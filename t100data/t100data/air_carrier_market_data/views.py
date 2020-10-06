# Create your views here.
import pdb
from django.views.generic import ListView
from django.db.models import Max, Sum, Avg, Min

from . models import MarketData

class MarketDataList(ListView):
    model = MarketData

# What are the top 5 airports in terms of: Total passengers by origin
class Top5AirportsPaxByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:5]
    template_name="rankorder_list_origin.html"

# What are the top 5 airports in terms of: Total passengers by destination
class Top5AirportsPaxByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_pax=Sum('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_destination.html"

#What are the top 5 airports in terms of: Total freight by origin
class Top5AirportsFreByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_fre=Sum('freight')) \
                        .order_by('-total_fre')[0:5]
    template_name="rankorder_list_freight_origin.html"

#What are the top 5 airports in terms of: Total freight by destination
class Top5AirportsFreByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_fre=Sum('freight')) \
                                 .order_by('-total_fre')[0:5]
    template_name="rankorder_list_freight_destination.html"

#What are the top 5 airports in terms of: Total mail by origin
class Top5AirportsMailByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:5]
    template_name="rankorder_list_mail_origin.html"

#What are the top 5 airports in terms of: Total mail by destination
class Top5AirportsMailByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_mail=Sum('mail')) \
                                 .order_by('-total_mail')[0:5]
    template_name="rankorder_list_mail_destination.html"

#What are the top 5 airports in terms of: Total distance by origin
class Top5AirportsDistanceByOrigin(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('orig_iata_code','orig_city_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:5]
    template_name="rankorder_list_distance_origin.html"

#What are the top 5 airports in terms of: Total distance by destination
class Top5AirportsDistanceByDestination(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .annotate(total_distance=Sum('distance')) \
                                 .order_by('-total_distance')[0:5]
    template_name="rankorder_list_distance_destination.html"

# Which airport reported the most passengers by month?
class TopPaxByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_pax_month.html"

    def get_queryset(self):

        month_list = []


        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_pax=Max('passengers')) \
                .order_by('-total_pax')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Which airport reported the longest distance by month?
class TopDistanceByMonth(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_origin_distance_month.html"

    def get_queryset(self):

        month_list = []


        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('orig_iata_code',
                        'orig_city_name',
                        'dest_iata_code',
                        'dest_city_name',
                        'month') \
                .filter(month__exact=month) \
                .annotate(total_distance=Max('distance')) \
                .order_by('-total_distance')[0:1]
            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

#Which airline reported the most freight carried?
class TopAirlineFreCarried(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name','orig_city_name') \
                        .annotate(total_fre=Sum('freight')) \
                        .order_by('-total_fre')[0:1]
    template_name="rankorder_list_freight_airline.html"


#Which airline reported the most passengers carried?
class TopAirlinePaxCarried(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name','orig_city_name') \
                        .annotate(total_pax=Sum('passengers')) \
                        .order_by('-total_pax')[0:1]
    template_name="rankorder_list_pax_airline.html"

#Which airline reported the most mail carried?
class TopAirlineMailCarried(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name','orig_city_name') \
                        .annotate(total_mail=Sum('mail')) \
                        .order_by('-total_mail')[0:1]
    template_name="rankorder_list_mail_airline.html"

#Which airline reported the longest flight distance?
class TopAirlineDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects \
                        .values('carrier_name','orig_city_name') \
                        .annotate(total_distance=Sum('distance')) \
                        .order_by('-total_distance')[0:1]
    template_name="rankorder_list_distance_airline.html"

#Rank order passengers carried, by month, for these airlines (AA)
class TopPaxByMonthByAirline_AA(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_pax_month_airline.html"

    def get_queryset(self):

        month_list = []


        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_name = 'American Airlines Inc.') \
                .annotate(total_pax=Max('passengers')) \
                .order_by('-total_pax')

            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

#Rank order passengers carried, by month, for these airlines (AlaskaA)
class TopPaxByMonthByAirline_AS(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_pax_month_airline.html"

    def get_queryset(self):

        month_list = []


        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_name = 'Alaska Airlines Inc.') \
                .annotate(total_pax=Max('passengers')) \
                .order_by('-total_pax')[0:1] 

            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

#Rank order passengers carried, by month, for these airlines (DL)
class TopPaxByMonthByAirline_DL(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_pax_month_airline.html"

    def get_queryset(self):

        month_list = []


        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_name = 'Delta Air Lines Inc.') \
                .annotate(total_pax=Max('passengers')) \
                .order_by('-total_pax')[0:1] 

            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

#Rank order passengers carried, by month, for these airlines (UA)
class TopPaxByMonthByAirline_UA(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_pax_month_airline.html"

    def get_queryset(self):

        month_list = []


        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_name = 'United Air Lines Inc.') \
                .annotate(total_pax=Max('passengers')) \
                .order_by('-total_pax')[0:1] 

            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

#Rank order passengers carried, by month, for these airlines (WN)
class TopPaxByMonthByAirline_WN(ListView):
    context_object_name = "airport_list"
    template_name="rankorder_list_pax_month_airline.html"

    def get_queryset(self):

        month_list = []


        # pdb.set_trace()

        # there are six months worth of data
        # not good ultimately as this is a "hard-coded" fore-knowledge of the data
        for month in range(1,7):
            queryset = MarketData.objects \
                .values('carrier_name',
                        'month') \
                .filter(month__exact=month) \
                .filter(carrier_name = 'Southwest Airlines Co.') \
                .annotate(total_pax=Max('passengers')) \
                .order_by('-total_pax')[0:1] 

            
            # off by one error for assignment

            month_list.append(queryset)

        # return list
        return month_list

# Average number of passengers with flights into destination airports (LAX)
class Avgpaxairport_LAX(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .filter(dest_iata_code = 'LAX') \
                                 .annotate(total_pax= Avg('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_avgpax_airport.html"

# Average number of passengers with flights into destination airports (SFO)
class Avgpaxairport_SFO(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .filter(dest_iata_code = 'SFO') \
                                 .annotate(total_pax= Avg('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_avgpax_airport.html"

# Average number of passengers with flights into destination airports (DFW)
class Avgpaxairport_DFW(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .filter(dest_iata_code = 'DFW') \
                                 .annotate(total_pax= Avg('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_avgpax_airport.html"

# Average number of passengers with flights into destination airports (ATL)
class Avgpaxairport_ATL(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .filter(dest_iata_code = 'ATL') \
                                 .annotate(total_pax= Avg('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_avgpax_airport.html"

# Average number of passengers with flights into destination airports (SFO)
class Avgpaxairport_ORD(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('dest_iata_code','dest_city_name') \
                                 .filter(dest_iata_code = 'ORD') \
                                 .annotate(total_pax= Avg('passengers')) \
                                 .order_by('-total_pax')[0:5]
    template_name="rankorder_list_avgpax_airport.html"

#Average volume of freight for flights departings MIA
class AvgFreAirport_MIA(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .filter(orig_iata_code = 'MIA') \
                                 .annotate(total_fre=Avg('freight')) \
                                 .order_by('-total_fre')[0:5]
    template_name="rankorder_list_avgfre_airport.html"

#Average volume of freight for flights departings MEM
class AvgFreAirport_MEM(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .filter(orig_iata_code = 'MEM') \
                                 .annotate(total_fre=Avg('freight')) \
                                 .order_by('-total_fre')[0:5]
    template_name="rankorder_list_avgfre_airport.html"

#Average volume of freight for flights departings JFK
class AvgFreAirport_JFK(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .filter(orig_iata_code = 'JFK') \
                                 .annotate(total_fre=Avg('freight')) \
                                 .order_by('-total_fre')[0:5]
    template_name="rankorder_list_avgfre_airport.html"

#Average volume of freight for flights departings ANC
class AvgFreAirport_ANC(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .filter(orig_iata_code = 'ANC') \
                                 .annotate(total_fre=Avg('freight')) \
                                 .order_by('-total_fre')[0:5]
    template_name="rankorder_list_avgfre_airport.html"

#Average volume of freight for flights departings SDF
class AvgFreAirport_SDF(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_iata_code','orig_city_name') \
                                 .filter(orig_iata_code = 'SDF') \
                                 .annotate(total_fre=Avg('freight')) \
                                 .order_by('-total_fre')[0:5]
    template_name="rankorder_list_avgfre_airport.html"

#What city pairs represent the most freight carried for the longest distance?
class CityPairsFreDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_city_name','dest_city_name') \
                                 .filter(freight__gt= 1) \
                                 .annotate(max_fre=Max('freight')) \
                                 .annotate(max_distance=Max('distance')) \
                                 .order_by('-distance','-max_fre',)[0:1]
    template_name="rankorder_list_maxfre_distance.html"

#What city pairs represent the most mail carried for the shortest distance?
class CityPairsMailDistance(ListView):
    context_object_name = "airport_list"
    queryset = MarketData.objects.values('orig_city_name','dest_city_name','mail') \
                                 .filter(distance = 1) \
                                 .annotate(min_distance=Min('distance')) \
                                 .order_by('min_distance','-mail')[0:1]
    template_name="rankorder_list_maxmail_distance.html"
