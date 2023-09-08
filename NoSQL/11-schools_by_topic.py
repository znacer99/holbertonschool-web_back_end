#!/usr/bin/env python3

"""
returns the list of school having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    function that returns list of school having specific topic
    """

    return mongo_collection.find({'topics': topic})
