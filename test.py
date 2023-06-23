import configparser
import json
import random
import time
from csv import reader
from datetime import datetime

#from kafka import KafkaProducer
from confluent_kafka import Producer
from confluent_kafka import SerializingProducer

from config.kafka import get_configs
from models.product import Product
from models.purchase import Purchase
from models.inventory import Inventory


# *** VARIABLES ***
products = []
propensity_to_buy_range = []


def main():
    create_product_list()
    #generate_sales()


# create products and propensity_to_buy lists from CSV data file
def create_product_list():
    with open("data/products.csv", "r") as csv_file:
        next(csv_file)  # skip header row
        csv_reader = reader(csv_file)
        csv_products = list(csv_reader)

    for p in csv_products:
        new_product = Product(
            str(datetime.utcnow()),
            p[0],
            p[1],
            p[2],
            p[3],
            p[4],
            p[5],
            p[6],
            p[14],
        )
    

    