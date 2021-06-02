#Code principal par B.Marduel - fevrier 2018
import processing
import sys
import os
import os.path
import datetime
import time

from qgis.core import (QgsProcessingAlgorithm,
       QgsProcessingParameterNumber,
       QgsProcessingParameterField,
       QgsProcessingParameterFeatureSource,
       QgsProcessingParameterFeatureSink,
       QgsProcessingParameterFolderDestination,
       QgsField,
       QgsFields)


class algTest(QgsProcessingAlgorithm):
    INPUT_VECTOR_REGARD = 'INPUT_VECTOR_REGARD'
    INPUT_VECTOR_RESEAU = 'INPUT_VECTOR_RESEAU'
    INPUT_ID_REGARD='ID_REGARD'
    INPUT_ALTITUDE_REGARD='ALTITUDE_REGARD'
    INPUT_PROFONDEUR_REGARD='PROFONDEUR_REGARD'
    INPUT_ID_CANA='ID_CANA'
    INPUT_NOEUD_AMONT_CANA='NOEUD_AMONT_CANA'    
    INPUT_NOEUD_AVAL_CANA='NOEUD_AVAL_CANA'
    INPUT_LONGUEUR_CANA='LONGUEUR_CANA'
    INPUT_DIAMETRE_CANA='DIAMETRE_CANA'
    INPUT_RUGOSITE_CANA='RUGOSITE_CANA'      
    
    def __init__(self):
        super().__init__()

    def name(self):
        return "Exports"

    def displayName(self):
        return "Export Epaswmm"

    def createInstance(self):
        return type(self)()

    def initAlgorithm(self, config=None):
        #ici on décrit les paramétrages utilisateur d'entrée et sortie de l'algorithme
        self.addParameter(
            QgsProcessingParameterFeatureSource(self.INPUT_VECTOR_REGARD,"Couche_des_regards",)
        )
        self.addParameter(
            QgsProcessingParameterField("RegardID",description="Champ IDENTIFIANT des regards",parentLayerParameterName="INPUT_VECTOR_REGARD")
        )
        self.addParameter(
            QgsProcessingParameterField(
                "RegardALTITUDE",
                description="Champ ALTITUDE des regards",
                parentLayerParameterName="INPUT_VECTOR_REGARD",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "RegardPROFONDEUR",
                description="Champs PROFONDEUR des regards",
                parentLayerParameterName="INPUT_VECTOR_REGARD",
            )
        )
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT_VECTOR_RESEAU,
                "Couche des réseaux",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "CanaID",
                description="Champ IDENTIFIANT des canalisations",
                parentLayerParameterName="INPUT_VECTOR_RESEAU",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "CanaIDNAMONT",
                description="Champ IDENTIFIANT NOEUD AMONT des canalisations",
                parentLayerParameterName="INPUT_VECTOR_RESEAU",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "CanaIDNAVAL",
                description="Champ IDENTIFIANT NOEUD AVAL des canalisations",
                parentLayerParameterName="INPUT_VECTOR_RESEAU",
            )
        )   
        self.addParameter(
            QgsProcessingParameterField(
                "CanaLONG",
                description="Champ LONGUEUR des Canalisations",
                parentLayerParameterName="INPUT_VECTOR_RESEAU",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "CanaDIAM",
                description="Champ DIAMETRE des Canalisations",
                parentLayerParameterName="INPUT_VECTOR_RESEAU",
            )
        )
        self.addParameter(
            QgsProcessingParameterField(
                "CanaRUGO",
                description="Champ RUGOSITE des Canalisations",
                parentLayerParameterName="INPUT_VECTOR_RESEAU",
            )
        )
        self.addParameter(
            QgsProcessingParameterFolderDestination(
                name="Dossiersortie",
                description="Répertoire de destination"
            )
        )
    def processAlgorithm(self, parameters, context, feedback):
        os.makedirs(
            parameters["Dossiersortie"],
            exist_ok=True
        )
        
        #DO SOMETHING
        #now = time.strftime("%c")
        i = datetime.datetime.now() 
        #file=open("D:/Users/bem/Desktop/OLDBUREAU/projet QGIS/QGISDEV/EXPORT_%s%s%s_%s%s%s"%(i.day,i.month,i.year,i.hour,i.minute,i.second)+".INP","w")
        file=open(parameters["Dossiersortie"]+"/EXPORT_%s%s%s_%s%s%s"%(i.day,i.month,i.year,i.hour,i.minute,i.second)+".INP","w")
        file.write("[TITLE]")
        file.write('\n'+";;Project Title/Notes")
        file.write('\n'+"")
        file.write('\n'+"[OPTIONS]")
        file.write('\n'+";;Option\tValue")
        file.write('\n'+"FLOW_UNITS\tLPS")
        file.write('\n'+"INFILTRATION\tHORTON")
        file.write('\n'+"FLOW_ROUTING\tDYNWAVE")
        file.write('\n'+"LINK_OFFSETS\tDEPTH")
        file.write('\n'+"MIN_SLOPE\t0")
        file.write('\n'+"ALLOW_PONDING\tNO")
        file.write('\n'+"SKIP_STEADY_STATE\tNO")
        file.write('\n'+"")
        file.write('\n'+"START_DATE\t%s/%s/%s"%(i.day, i.month, i.year))
        file.write('\n'+"START_TIME\t00:00:00")
        file.write('\n'+"REPORT_START_DATE\t%s/%s/%s"%(i.day, i.month, i.year))
        file.write('\n'+"REPORT_START_TIME\t00:00:00")
        file.write('\n'+"END_DATE\t%s/%s/%s"%(i.day, i.month, i.year))
        file.write('\n'+"END_TIME\t23:00:00")
        file.write('\n'+"SWEEP_START\t1/1")
        file.write('\n'+"SWEEP_END\t12/31")
        file.write('\n'+"DRY_DAYS\t0")
        file.write('\n'+"REPORT_STEP\t00:05:00")
        file.write('\n'+"WET_STEP\t00:05:00")
        file.write('\n'+"DRY_STEP\t01:00:00")
        file.write('\n'+"ROUTING_STEP\t0:00:10")
        file.write('\n'+"")
        file.write('\n'+"INERTIAL_DAMPING\tPARTIAL")
        file.write('\n'+"NORMAL_FLOW_LIMITED\tBOTH")
        file.write('\n'+"FORCE_MAIN_EQUATION\tH-W")
        file.write('\n'+"VARIABLE_STEP\t0.75")
        file.write('\n'+"LENGTHENING_STEP\t0")
        file.write('\n'+"MIN_SURFAREA\t1.14")
        file.write('\n'+"MAX_TRIALS\t8")
        file.write('\n'+"HEAD_TOLERANCE\t0.0015")
        file.write('\n'+"SYS_FLOW_TOL\t5")
        file.write('\n'+"LAT_FLOW_TOL\t5")
        file.write('\n'+"MINIMUM_STEP\t0.5")
        file.write('\n'+"THREADS\t1")
        file.write('\n'+"")
        file.write('\n'+"[EVAPORATION]")
        file.write('\n'+";;Data Source   	Parameters")
        file.write('\n'+";;--------------	----------------")
        file.write('\n'+"CONSTANT\t0.0")
        file.write('\n'+"DRY_ONLY\tNO")
        file.write('\n'+"")
        file.write('\n'+"[JUNCTIONS]")
        file.write('\n'+";;Name          	Elevation 	MaxDepth  	InitDepth 	SurDepth  	Aponded")
        file.write('\n'+";;--------------	----------	----------	----------	----------	----------")

#Creation de la boucle pour traiter lles regards de 1 a nb regard (variable feats_count_regard)
        layerregards = self.parameterAsVectorLayer(parameters, self.INPUT_VECTOR_REGARD, context)
        iter = layerregards.getFeatures()
        idx= layerregards.fields().indexFromName('RegardID')
        #idx1= layerregards.fields().indexFromName("RegardALTITUDE")
        #idx2= layerregards.fields().indexFromName("RegardPROFONDEUR")
        for field in layerregards.fields():
            file.write('\n'+field.name())
        for feature in iter:
            attrs = feature.attributes()
            file.write('\n'+str(attrs[idx]))#+"\t"+str(attrs[idx1]))#+"\t"+attrs[idx2]#+"\t0\t0\t0")
        file.close()
