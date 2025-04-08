from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaError
import json
import asyncio
from sqlalchemy.orm import Session
from app.models.patientModel import Patient


class PatientConsumer:
    def __init__(self, bootstrap_servers, db: Session) :
        self.consumer = AIOKafkaConsumer(
            "patient_creation",
            bootstrap_servers=bootstrap_servers,
            group_id="patient_creation_group",
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        
        self.db = db
        
    async def start(self):
        try:
            await self.consumer.start()
            while True:
                try:
                    async for message in self.consumer:
                        await self.process_message(message.value)
                except KafkaError as e:
                    print(f"Kafka error: {e}, retrying...")
                    await asyncio.sleep(5)
        finally:
            await self.consumer.stop()

    async def process_message(self, message):
        if message['event_type'] == 'user_created':
            user_data = message['user_data']
            # Process the user data
            try:
                new_patient = Patient(
                    user_id=user_data['user_id'],
                    username=user_data['username'],
                    is_active=True
                )
                self.db.add(new_patient)
                self.db.commit()
                self.db.refresh(new_patient)
                print(f"patient created: {new_patient.username}")
            except Exception as e:
                print(f"Error processing user creation: {str(e)}")