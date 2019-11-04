#!/usr/bin/env python
import requests
import json

# Pool class has attributes name, pool id, and inventory (a list of dictionaries: dict = {"machine": ws-####-##, "status": status})
class Pool:
    name = None
    pool_id = None
    inventory = {}

    def __init__(self, name, pool_id, inventory):
        self.name = name[7:] # from after "shared-" to end of string
        self.pool_id = pool_id
        self.inventory = inventory

    def __repr__(self):
        return self.name

# ------------------------------------------------------------------------------
# GET
