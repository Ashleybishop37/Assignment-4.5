# urls.py
from django.urls import path
from . views import MarketDataList, \
                    Top5AirportsPaxByOrigin, \
                    Top5AirportsPaxByDestination, \
                    TopDistanceByMonth, \
                    Top5AirportsFreByOrigin, \
                    Top5AirportsFreByDestination, \
                    Top5AirportsMailByOrigin, \
                    Top5AirportsMailByDestination, \
                    Top5AirportsDistanceByOrigin, \
                    Top5AirportsDistanceByDestination, \
                    TopPaxByMonth, \
                    TopAirlineFreCarried, \
                    TopAirlinePaxCarried, \
                    TopAirlineMailCarried, \
                    TopAirlineDistance, \
                    TopPaxByMonthByAirline_AA, \
                    TopPaxByMonthByAirline_AS, \
                    TopPaxByMonthByAirline_DL, \
                    TopPaxByMonthByAirline_UA, \
                    TopPaxByMonthByAirline_WN, \
                    Avgpaxairport_LAX, \
                    Avgpaxairport_SFO, \
                    Avgpaxairport_DFW, \
                    Avgpaxairport_ATL, \
                    Avgpaxairport_ORD, \
                    AvgFreAirport_MIA, \
                    AvgFreAirport_MEM, \
                    AvgFreAirport_JFK, \
                    AvgFreAirport_ANC, \
                    AvgFreAirport_SDF, \
                    CityPairsFreDistance, \
                    CityPairsMailDistance


urlpatterns = [
    path('list/', MarketDataList.as_view(), name="list"),
    path('top5paxorigin/', 
        Top5AirportsPaxByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Origin Airport"}
        ),
        name="top5paxorigin"),
    path('top5paxdestination/',  
        Top5AirportsPaxByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Passengers by Destination Airport"}
        ), 
        name="top5paxdestination"),
    path('topdistance_month/',  
        TopDistanceByMonth.as_view(
            extra_context={'title': "Top Distance by Month"}
        ), 
        name="topdistance_month"),
    path('top5freight_origin/',  
        Top5AirportsFreByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Origin Airport"}
        ), 
        name="top5freight_origin"),
    path('top5fredestination/',
        Top5AirportsFreByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Freight by Destination Airport"}
        ),
        name="top5fredestination"),
     path('top5mailorigin/',  
        Top5AirportsMailByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Origin Airport"}
        ), 
        name="top5mailorigin"),
    path('top5maildestination/',
        Top5AirportsMailByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Mail by Destination Airport"}
        ),
        name="top5maildestination"),
    path('top5distanceorigin/',  
        Top5AirportsDistanceByOrigin.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Origin Airport"}
        ), 
        name="top5distanceorigin"),
    path('top5distancedestination/',
        Top5AirportsDistanceByDestination.as_view(
            extra_context={'title': "Top 5 Airports - Distance by Destination Airport"}
        ),
        name="top5distancedestination"),
    path('toppax_month/',  
        TopPaxByMonth.as_view(
            extra_context={'title': "Top Passengers by Month"}
        ), 
        name="toppax_month"),
    path('topfre_airline/',  
        TopAirlineFreCarried.as_view(
            extra_context={'title': "Top Airline Carrying the Most Freight"}
        ), 
        name="topfre_airline"),
    path('toppax_airline/',  
        TopAirlinePaxCarried.as_view(
            extra_context={'title': "Top Airline Carrying the Most Passengers"}
        ), 
        name="toppax_airline"),
    path('topmail_airline/',  
        TopAirlineMailCarried.as_view(
            extra_context={'title': "Top Airline Carrying the Most Mail"}
        ), 
        name="topmail_airline"),
    path('topdistance_airline/',  
        TopAirlineDistance.as_view(
            extra_context={'title': "Top Airline Flying the Longest Distance"}
        ), 
        name="topdistance_airline"),
    path('toppaxmonth_airline/',  
        TopPaxByMonthByAirline_AA.as_view(
            extra_context={'title': "American Airlines Passengers Carried by Month"}
        ), 
        name="toppaxmonth_airline"),
    path('toppaxmonth_airline_AS/',  
        TopPaxByMonthByAirline_AS.as_view(
            extra_context={'title': "Alaska Airlines Passengers Carried by Month"}
        ), 
        name="toppaxmonth_airline_AS"),
    path('toppaxmonth_airline_DL/',  
        TopPaxByMonthByAirline_DL.as_view(
            extra_context={'title': "Delta Airlines Passengers Carried by Month"}
        ), 
        name="toppaxmonth_airline_DL"),
    path('toppaxmonth_airline_UA/',  
        TopPaxByMonthByAirline_UA.as_view(
            extra_context={'title': "United Airlines Passengers Carried by Month"}
        ), 
        name="toppaxmonth_airline_UA"),
    path('toppaxmonth_airline_WN/',  
        TopPaxByMonthByAirline_WN.as_view(
            extra_context={'title': "Southwest Airlines Passengers Carried by Month"}
        ), 
        name="toppaxmonth_airline_WN"),
    path('avgpaxmonth_airline_LAX/',  
        Avgpaxairport_LAX.as_view(
            extra_context={'title': "Average Number Of Passangers for Flights into LAX"}
        ), 
        name="avgpaxmonth_airline_LAX"),
    path('avgpaxmonth_airline_SFO/',  
        Avgpaxairport_SFO.as_view(
            extra_context={'title': "Average Number Of Passangers for Flights into SFO"}
        ), 
        name="avgpaxmonth_airline_SFO"),
    path('avgpaxmonth_airline_DFW/',  
        Avgpaxairport_DFW.as_view(
            extra_context={'title': "Average Number Of Passangers for Flights into DFW"}
        ), 
        name="avgpaxmonth_airline_DFW"),
    path('avgpaxmonth_airline_ATL/',  
        Avgpaxairport_ATL.as_view(
            extra_context={'title': "Average Number Of Passangers for Flights into ATL"}
        ), 
        name="avgpaxmonth_airline_ATL"),
    path('avgpaxmonth_airline_ORD/',  
        Avgpaxairport_ORD.as_view(
            extra_context={'title': "Average Number Of Passangers for Flights into ORD"}
        ), 
        name="avgpaxmonth_airline_ORD"),
    path('avgfremonth_airline_MIA/',  
        AvgFreAirport_MIA.as_view(
            extra_context={'title': "Average Volume of Freight for Flights Departing from MIA"}
        ), 
        name="avgfremonth_airline_MIA"),
    path('avgfremonth_airline_MEM/',  
        AvgFreAirport_MEM.as_view(
            extra_context={'title': "Average Volume of Freight for Flights Departing from MEM"}
        ), 
        name="avgfremonth_airline_MEM"),
    path('avgfremonth_airline_JFK/',  
        AvgFreAirport_JFK.as_view(
            extra_context={'title': "Average Volume of Freight for Flights Departing from JFK"}
        ), 
        name="avgfremonth_airline_JFK"),
    path('avgfremonth_airline_ANC/',  
        AvgFreAirport_ANC.as_view(
            extra_context={'title': "Average Volume of Freight for Flights Departing from ANC"}
        ), 
        name="avgfremonth_airline_ANC"),
    path('avgfremonth_airline_SDF/',  
        AvgFreAirport_SDF.as_view(
            extra_context={'title': "Average Volume of Freight for Flights Departing from SDF"}
        ), 
        name="avgfremonth_airline_SDF"),
    path('maxfre_citypairs/',  
        CityPairsFreDistance.as_view(
            extra_context={'title': "City Pairs that represent the most freight carried for the longest distance"}
        ), 
        name="maxfre_citypairs"),
    path('maxmail_citypairs/',  
        CityPairsMailDistance.as_view(
            extra_context={'title': "City Pairs that represent the most mail carried for the shortest distance"}
        ), 
        name="maxmail_citypairs"),
]

