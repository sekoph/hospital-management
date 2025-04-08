from aiokafka import AIOKafkaProducer
import json
import asyncio
import uuid
from datetime import datetime

class UserProducer:
    def __init__(self, bootstrap_servers):
        self.producer = AIOKafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        
    async def start(self):
        await self.producer.start()
        
    async def stop(self):
        await self.producer.stop()
    
    async def send_user_creation_event(self, user_data):
        topic = "docter_creation" if user_data['role'] == 'doctor' else "patient_creation"
        
        message ={
            "event_id": str(uuid.uuid4()),
            "event_type": "user_created",
            "time_stamp": datetime.datetime.now().isoformat(),
            "user_data": {
                "user_id": user_data['user_id'],
                "role": user_data['role'],
                "username": user_data['username']
            }
        }
        
        await self.producer.send_and_wait(topic, message)