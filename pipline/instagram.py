__author__ = 'jsiraco'

import settings


class InstagramPipline():

    data = {}

    def __init__(self):
        """
        Logs in, sets needed variables to get instagram data
        :return:
        """

        # TODO: Add login and data grab logic

    def run(self):
        """
        Runs the pipeline
        grabs data about posts and adds it to the data JSON object
        :return:
        """

        # TODO: Logic to get data, enforce request limits, and filter out duplicates

    def save(self):
        """
        Downloads and saves instagram content(MongoDB?)
        :return:
        """

        # TODO:Find place to save data, write logic to save images(Filter out video?)