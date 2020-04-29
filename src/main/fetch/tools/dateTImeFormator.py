import datetime
import pytz


class DateTimeFormator:

    def __init__(self, string):
        self.date_time_str = string

    def nzHerald(self):
        dateTimeList = self.date_time_str.split(" ")

        newsDate = dateTimeList[0]
        newsMonth = dateTimeList[1].replace(',', '')
        newsYear = dateTimeList[2]
        newsTime = dateTimeList[3].upper()
        rawPostDateTime = "%(newsMonth)s %(newsDate)s %(newsYear)s %(newsTime)s" % {"newsMonth": newsMonth,
                                                                                    "newsDate": newsDate,
                                                                                    "newsYear": newsYear,
                                                                                    "newsTime": newsTime}
        try:
            postDateTimeObj = datetime.datetime.strptime(rawPostDateTime, '%b %d %Y %I:%M%p')
        except:
            postDateTimeObj = datetime.datetime.strptime(datetime.datetime.now, '%b %d %Y %I:%M%p')
        nztz = pytz.timezone('Pacific/Auckland')
        utctz = pytz.timezone("UTC")
        nz_date_time_obj = nztz.localize(postDateTimeObj)
        utc_datetime_obj = nz_date_time_obj.astimezone(utctz)
        utc_datetime_string = utc_datetime_obj.strftime('%Y-%m-%d %H:%M:%S%z')

        return utc_datetime_string
