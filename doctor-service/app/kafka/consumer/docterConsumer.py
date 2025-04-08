from aiokafka import AioKafkaConsumer
import json
import asyncio
from sqlalchemy.orm import Session
from app.models.doctorModel import Doctor


class DocterConsumer:
    def __init__(self, bootstrap_servers, db: Session) :
        self.consumer = AioKafkaConsumer(
            "docter_creation",
            bootstrap_servers=bootstrap_servers,
            group_id="docter_creation_group",
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        
        self.db = db
        
    async def start(self):
        await self.consumer.start()
        try:
            async for message in self.consumer:
                await self.process_message(message.value)
        finally:
            await self.consumer.stop()

    async def process_message(self, message):
        if message['event_type'] == 'user_created':
            user_data = message['user_data']
            # Process the user data
            try:
                new_docter = Doctor(
                    user_id=user_data['user_id'],
                    username=user_data['username'],
                    role=user_data['role'],
                    is_active=True
                )
                self.db.add(new_docter)
                self.db.commit()
                self.db.refresh(new_docter)
                print(f"Doctor created: {new_docter.username}")
            except Exception as e:
                print(f"Error processing user creation: {str(e)}")