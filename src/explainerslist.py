from flask_restful import Resource

class Explainers(Resource):
    def get(self):
        return [ 
                 '/Images/Anchors',
                 '/Images/ClassificationReport',
                 '/Images/ConfusionMatrix',
                 '/Images/GradCam',
                 '/Images/IntegratedGradients',
                 '/Images/LIME',
                 '/Images/SSIMCounterfactuals',
                 '/Images/SSIMNearestNeighbours',
                 '/Timeseries/ConfusionMatrix',
                 '/Timeseries/LEFTIST',
                 '/Timeseries/LIMESegment',
                 '/Timeseries/NativeGuides',
                 '/Timeseries/NearestNeighbours',
                 '/Timeseries/NEVES',
                 '/Timeseries/SummaryMetrics'
                 
               ]

