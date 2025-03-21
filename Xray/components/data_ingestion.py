import sys

from Xray.cloud_storage.s3_operation import S3Operation
# from Xray.constant.trainingpipeline import *
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.artifact_entity import DataIngestionConfig
from Xray.exception import XRayException
from Xray.logger import logging


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.s3 = S3Operation()

    def get_data_from_s3(self):
        try:
            logging.info("Enter the get_data_from_s3 method of Data Ingestion Class")

            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder,

            )


        except Exception as e:
            raise XRayException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise XRayException(e,sys)


