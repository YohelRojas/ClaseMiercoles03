from flask_restful import Resource
from controllers.health.controller import HealthController
from controllers.issueId.controller import IssueByIdController
from controllers.lab.controller import LabController
from flask_restful import Api


def addServiceLayer(api: Api):
    # Health
    api.add_resource(HealthController, HealthController.route)
    # Lab
    api.add_resource(LabController, LabController.route)

    # Issue
    api.add_resource(IssueByIdController, IssueByIdController.route)

