from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from .apps import WebappConfig

class call_model(APIView):

	def __init__(self):
		self.graderRef = WebappConfig.grader

	def gradeFun(self, Type, Data):

		if Type == "Type1":
			if len(Data) < 10:
				if len(Data) < 5:
					Grade = [0, 0, len(Data)]
				else:
					Grade = [0, len(Data), 0]
			else:
				Grade = self.graderRef(Data, "Type1")

		if Type == "Type2":
			if len(Data) < 10:
				if len(Data) < 5:
					Grade = [0, 0, len(Data)]
				else:
					Grade = [0, len(Data), 0]
			else:
				Grade = self.graderRef(Data, "Type2")

		if Type == "Type3":
			if len(Data) < 2:
				if len(Data) < 1:
					Grade = [0, 0, len(Data)]
				else:
					Grade = [0, len(Data), 0]
			else:
				Grade = self.graderRef(Data, "Type3")

		if Type == "Type4":
			if len(Data) < 10:
				if len(Data) < 5:
					Grade = [0, 0, len(Data)]
				else:
					Grade = [0, len(Data), 0]
			else:
				Grade = self.graderRef(Data, "Type4")

		if Type == "Type5":
			if len(Data) < 1:
				Grade = [0, 0, len(Data)]
			else:
				Grade = self.graderRef(Data, "Type5")

		if Type == "Type6":
			if len(Data) < 1:
				Grade = [0, 0, len(Data)]
			else:
				Grade = self.graderRef(Data, "Type6")
		
		return Grade

	def calculateScore(self, Grade):
		low = 8.32
		mid = 4.99
		high = 1.66
		sentenceNum = Grade[0] + Grade[1] + Grade[2]

		if sentenceNum == 0:
			return 0;
		else:
			catScore = low * Grade[0] + mid * Grade[1] + high * Grade[2]
			catScore = int(catScore / sentenceNum * 10)
			return catScore


	def post(self, request):
		# Fetch Link from GUI in string(weblink)
		RawData = JSONParser().parse(request)

		Type = RawData["Type"]
		Data = RawData["Data"]

		print("Type :: ", Type)
		print("Type of Data :: ", type(Data))

		# Grade the Data
		Grade = self.gradeFun(Type, Data)
		print("Grade :: ", Grade)
		print("Graded Successfully")
		
		# Calculate final scores
		finalScore = self.calculateScore(Grade)
		# print(finalScores)
		print("All Done!!!!")
		
		return JsonResponse({"Percentage" : finalScore}, status = 201)