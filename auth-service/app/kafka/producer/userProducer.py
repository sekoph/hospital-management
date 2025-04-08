from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError
import json
import asyncio
import uuid
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

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
        topic = "doctor_creation" if user_data['role'] == 'doctor' else "patient_creation"

        try:
            # Ensure producer is started
            await self.producer.start()

            # Refresh metadata by fetching topics from the cluster
            metadata = await self.producer.partitions_for(topic)

            if metadata is None or len(metadata) == 0:
                logger.warning(f"Topic '{topic}' does not exist.")
                logger.info(f"Kafka may be set to auto-create topics. Proceeding anyway.")

            # Create the message
            message = {
                "event_id": str(uuid.uuid4()),
                "event_type": "user_created",
                "time_stamp": datetime.now().isoformat(),
                "user_data": {
                    "user_id": user_data['user_id'],
                    "username": user_data['username']
                }
            }

            # Send the message
            await self.producer.send_and_wait(topic, message)
            logger.info(f"Message sent to topic '{topic}'.")
            print(f"message {message} sent: {topic} topic")


        except KafkaError as e:
            logger.error(f"Kafka error while sending to topic '{topic}': {e}")
            raise

        finally:
            await self.producer.stop()