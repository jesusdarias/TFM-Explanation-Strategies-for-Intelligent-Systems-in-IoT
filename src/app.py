import sys
import os
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from explainerslist import Explainers

from resources.explainers.images.lime import LimeImage
from resources.explainers.images.anchors import AnchorsImage
from resources.explainers.images.gradcam import GradCam
from resources.explainers.images.integratedGradients import IntegratedGradientsImage
from resources.explainers.images.confusionMatrix import ConfusionMatrixImages
from resources.explainers.images.classificationReport import ClassificationReport
from resources.explainers.images.nnSSIM import SSIMNearestNeighbours
from resources.explainers.images.cfSSIM import SSIMCounterfactual
from resources.explainers.timeseries.limeSegment import LimeSegment
from resources.explainers.timeseries.leftist import Leftist
from resources.explainers.timeseries.neves import Neves
from resources.explainers.timeseries.nearestNeighbours import TSNearestNeighbours
from resources.explainers.timeseries.nativeGuides import NativeGuides
from resources.explainers.timeseries.confusionMatrix import TSConfusionMatrix
from resources.explainers.timeseries.summaryMetrics import TSSummaryMetrics



MODEL_FOLDER="Models"
UPLOAD_FOLDER="Uploads"
if len(sys.argv) > 3 :
    raise Exception("Too many arguments passed to the program")
else:
    if len(sys.argv) >= 2 :
        if os.path.exists(sys.argv[1]):
            if os.path.isdir(sys.argv[1]):
                print("Using existing directory '" +sys.argv[1]+ "'")
            else:
                raise Exception("A non-directory file named '" + sys.argv[1]+ "' already exists. Please use another name.")
        else:
            os.mkdir(sys.argv[1])
            print("The '" +sys.argv[1]+ "' directory was created.")
        MODEL_FOLDER=sys.argv[1]
    else:
        if os.path.exists(MODEL_FOLDER):
            if os.path.isdir(MODEL_FOLDER):
                print("Using existing default directory '" +MODEL_FOLDER+ "'")
            else:
                raise Exception("A non-directory file named '" + MODEL_FOLDER+ "' already exists. Please use another name.")
        else:
            os.mkdir(MODEL_FOLDER)
            print("The '" +MODEL_FOLDER+ "' default directory was created.")

    if len(sys.argv) == 3:
        if os.path.exists(sys.argv[2]):
            if os.path.isdir(sys.argv[2]):
                print("Using existing directory '" +sys.argv[2]+ "'")
            else:
                raise Exception("A non-directory file named '" + sys.argv[2]+ "' already exists. Please use another name.")
        else:
            os.mkdir(sys.argv[2])
            print("The '" +sys.argv[2]+ "' directory was created.")
        UPLOAD_FOLDER=sys.argv[2]
    else:
        if os.path.exists(UPLOAD_FOLDER):
            if os.path.isdir(UPLOAD_FOLDER):
                print("Using existing default directory '" +UPLOAD_FOLDER+ "'")
            else:
                raise Exception("A non-directory file named '" + UPLOAD_FOLDER+ "' already exists. Please use another name.")
        else:
            os.mkdir(UPLOAD_FOLDER)
            print("The '" +UPLOAD_FOLDER+ "' default directory was created.")
path_dict={"model_folder":MODEL_FOLDER,"upload_folder":UPLOAD_FOLDER}
    
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None
app = Flask(__name__)


app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)
api = Api(app)
api.add_resource(Explainers,'/Explainers')
api.add_resource(LimeImage, '/Images/LIME','/Images/LIME/<id>',resource_class_kwargs=path_dict)
api.add_resource(AnchorsImage, '/Images/Anchors','/Images/Anchors/<id>',resource_class_kwargs=path_dict)
api.add_resource(ClassificationReport, '/Images/ClassificationReport','/Images/ClassificationReport/<id>',resource_class_kwargs=path_dict)
api.add_resource(GradCam, '/Images/GradCam','/Images/GradCam/<id>',resource_class_kwargs=path_dict)
api.add_resource(IntegratedGradientsImage, '/Images/IntegratedGradients','/Images/IntegratedGradients/<id>',resource_class_kwargs=path_dict)
api.add_resource(ConfusionMatrixImages, '/Images/ConfusionMatrix','/Images/ConfusionMatrix/<id>',resource_class_kwargs=path_dict)
api.add_resource(SSIMNearestNeighbours, '/Images/SSIMNearestNeighbours','/Images/SSIMNearestNeighbours/<id>',resource_class_kwargs=path_dict)
api.add_resource(SSIMCounterfactual, '/Images/SSIMCounterfactuals','/Images/SSIMCounterfactuals/<id>',resource_class_kwargs=path_dict)
api.add_resource(LimeSegment, "/Timeseries/LIMESegment",'/Timeseries/LIMESegment/<id>', resource_class_kwargs=path_dict)
api.add_resource(Leftist, "/Timeseries/LEFTIST",'/Timeseries/LEFTIST/<id>', resource_class_kwargs=path_dict)
api.add_resource(Neves, "/Timeseries/NEVES",'/Timeseries/NEVES/<id>', resource_class_kwargs=path_dict)
api.add_resource(NativeGuides, "/Timeseries/NativeGuides",'/Timeseries/NativeGuides/<id>', resource_class_kwargs=path_dict)
api.add_resource(TSNearestNeighbours, "/Timeseries/NearestNeighbours",'/Timeseries/NearestNeighbours/<id>', resource_class_kwargs=path_dict)
api.add_resource(TSConfusionMatrix, "/Timeseries/ConfusionMatrix",'/Timeseries/ConfusionMatrix/<id>', resource_class_kwargs=path_dict)
api.add_resource(TSSummaryMetrics, "/Timeseries/SummaryMetrics",'/Timeseries/SummaryMetrics/<id>', resource_class_kwargs=path_dict)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
