from __future__ import unicode_literals
from django.db import models

class AirlineSearch(models.Model):
    airline = models.TextField()

    class Meta:

        db_table = "airlines" 

    def __unicode__(self):
        return self.airline

class AirportSearch(models.Model):
    both = models.TextField()
    location = models.TextField()

    class Meta:
        
        db_table = 'airports'

    def __unicode__(self):
        return self.both + " " + self.location

class AirportInfo(models.Model):
    code = models.CharField(max_length=3)
    airport = models.TextField()
    both = models.TextField()
    location = models.TextField()

    class Meta:
        
        db_table = 'airports'

    def __unicode__(self):
        return "{0}, {1}, {2}, {3}".format(self.code, self.airport, self.both, self.location)

class AirportMixin(object):
    def __unicode__(self):
        return "%s,%s,%s,%s,%s," % (self.airline, self.airline_iata, self.departures_terminal, self.arrivals_terminal, self.term_or_con)

class Abe(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()

    class Meta:
        
        db_table = 'ABE'

class Abi(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()

    class Meta:
        
        db_table = 'ABI'


class Abq(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()

    class Meta:
        
        db_table = 'ABQ'


class Aby(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ABY'


class Ack(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ACK'


class Act(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ACT'


class Acv(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ACV'


class Acy(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ACY'


class Aex(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AEX'


class Ags(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AGS'


class Ahn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AHN'


class Alb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ALB'


class Ama(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AMA'


class Anc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ANC'


class Art(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ART'


class Ase(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ASE'


class Atl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ATL'


class Atw(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ATW'


class Aus(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AUS'


class Avl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AVL'


class Avp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AVP'


class Aza(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AZA'


class Azo(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'AZO'


class Bdl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BDL'


class Bfl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BFL'


class Bgm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BGM'


class Bgr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BGR'


class Bhb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BHB'


class Bhm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BHM'


class Bil(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BIL'


class Bli(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BLI'


class Bmi(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BMI'


class Bna(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BNA'


class Boi(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BOI'


class Bos(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BOS'


class Bpt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BPT'


class Bqk(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BQK'


class Bro(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BRO'


class Btr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BTR'


class Btv(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BTV'


class Buf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BUF'


class Bur(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BUR'


class Bwi(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BWI'


class Bzn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'BZN'


class Cae(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CAE'


class Cak(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CAK'


class Cdc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CDC'


class Cha(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CHA'


class Cho(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CHO'


class Chs(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CHS'


class Cid(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CID'


class Cle(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CLE'


class Clt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CLT'


class Cmh(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CMH'


class Cmi(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CMI'


class Cos(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'COS'


class Cpr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CPR'


class Crp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CRP'


class Crq(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CRQ'


class Crw(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CRW'


class Csg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CSG'


class Cvg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CVG'


class Cwa(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CWA'


class Cys(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'CYS'


class Dab(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DAB'


class Dal(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DAL'


class Day(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DAY'


class Dca(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DCA'


class Den(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DEN'


class Dfw(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DFW'


class Dlh(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DLH'


class Dro(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DRO'


class Dsm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DSM'


class Dtw(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'DTW'


class Ecp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ECP'


class Ege(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'EGE'


class Elm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ELM'


class Elp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ELP'


class Eri(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ERI'


class Eug(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'EUG'


class Evv(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'EVV'


class Ewn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'EWN'


class Ewr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'EWR'


class Eyw(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'EYW'


class Fai(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FAI'


class Far(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FAR'


class Fat(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FAT'


class Fay(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FAY'


class Flg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FLG'


class Fll(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FLL'


class Flo(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FLO'


class Fnt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FNT'


class Fsd(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FSD'


class Fwa(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'FWA'


class Gcn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GCN'


class Geg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GEG'


class Gfk(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GFK'


class Gjt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GJT'


class Gnv(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GNV'


class Gpi(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GPI'


class Gpt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GPT'


class Grb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GRB'


class Grk(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GRK'


class Grr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GRR'


class Gso(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GSO'


class Gsp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GSP'


class Gtf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GTF'


class Gyy(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'GYY'


class Hdn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HDN'


class Hgr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HGR'


class Hln(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HLN'


class Hnl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HNL'


class Hou(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HOU'


class Hpn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HPN'


class Hrl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HRL'


class Hsv(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HSV'


class Hts(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HTS'


class Hvn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'HVN'


class Iad(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'IAD'


class Iah(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'IAH'


class Ict(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ICT'


class Ida(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'IDA'


class Ifp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'IFP'


class Ilg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ILG'


class Ilm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ILM'


class Ind(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'IND'


class Inl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'INL'


class Ipl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'IPL'


class Ipt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'IPT'


class Isn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ISN'


class Isp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ISP'


class Ith(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ITH'


class Ito(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ITO'


class Jac(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'JAC'


class Jan(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'JAN'


class Jax(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'JAX'


class Jfk(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()

    class Meta:
        
        db_table = 'JFK'


class Jnu(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'JNU'


class Koa(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'KOA'


class Lan(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LAN'


class Las(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LAS'


class Lax(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LAX'


class Lbb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LBB'


class Lch(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LCH'


class Lex(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LEX'


class Lft(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LFT'


class Lga(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LGA'


class Lgb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LGB'


class Lih(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LIH'


class Lit(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LIT'


class Lnk(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LNK'


class Lrd(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LRD'


class Lws(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LWS'


class Lyh(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'LYH'


class Maf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MAF'


class Mbs(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MBS'


class Mci(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MCI'


class Mcn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MCN'


class Mco(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MCO'


class Mdt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MDT'


class Mdw(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MDW'


class Mem(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MEM'


class Mfe(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MFE'


class Mfr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MFR'


class Mgm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MGM'


class Mht(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MHT'


class Mia(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MIA'


class Mke(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MKE'


class Mlb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MLB'


class Mli(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MLI'


class Mlu(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MLU'


class Mob(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MOB'


class Mod(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MOD'


class Mot(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MOT'


class Mqt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MQT'


class Mry(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MRY'


class Msn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MSN'


class Mso(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MSO'


class Msp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MSP'


class Msy(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MSY'


class Myr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'MYR'


class Oaj(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'OAJ'


class Oak(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'OAK'


class Ogg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'OGG'


class Okc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'OKC'


class Oma(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'OMA'


class Ont(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ONT'


class Ord(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ORD'


class Orf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ORF'


class Orh(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ORH'


class Pah(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PAH'


class Pbi(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PBI'


class Pdx(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PDX'


class Pgv(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PGV'


class Phf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PHF'


class Phl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PHL'


class Phx(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PHX'


class Pia(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PIA'


class Pie(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PIE'


class Pit(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PIT'


class Pns(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PNS'


class Psp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PSP'


class Pub(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PUB'


class Pvd(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PVD'


class Pwm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'PWM'


class Rap(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RAP'


class Rdm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RDM'


class Rdu(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RDU'


class Rfd(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RFD'


class Ric(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RIC'


class Rno(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RNO'


class Roa(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ROA'


class Roc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'ROC'


class Rst(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RST'


class Rsw(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'RSW'


class Saf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SAF'


class San(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SAN'


class Sat(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SAT'


class Sav(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SAV'


class Sba(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SBA'


class Sbn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SBN'


class Sbp(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SBP'


class Sby(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SBY'


class Sce(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SCE'


class Sdf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SDF'


class Sea(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SEA'


class Sfb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SFB'


class Sff(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SFF'


class Sfo(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SFO'


class Sgf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SGF'


class Shd(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SHD'


class Shv(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SHV'


class Sjc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SJC'


class Sjt(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SJT'


class Sju(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SJU'


class Slc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SLC'


class Smf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SMF'


class Sna(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SNA'


class Srq(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SRQ'


class Stl(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'STL'


class Sts(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'STS'


class Sux(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SUX'


class Swf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SWF'


class Syr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'SYR'


class Teb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TEB'


class Tlh(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TLH'


class Tol(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TOL'


class Tpa(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TPA'


class Tri(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TRI'


class Ttn(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TTN'


class Tul(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TUL'


class Tus(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TUS'


class Tvc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TVC'


class Tys(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'TYS'


class Vny(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'VNY'


class Vps(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'VPS'


class Xna(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'XNA'


class Yeg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YEG'


class Yhm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YHM'


class Yhz(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YHZ'


class Ykf(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YKF'


class Ykm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YKM'


class Yng(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YNG'


class Yow(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YOW'


class Yqb(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YQB'


class Yqm(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YQM'


class Yqr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YQR'


class Yul(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YUL'


class Yvr(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YVR'


class Ywg(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YWG'


class Yxe(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YXE'


class Yyc(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YYC'


class Yyz(AirportMixin, models.Model):
    airline = models.TextField()
    airline_iata = models.CharField(max_length=2)
    departures_terminal = models.TextField()
    arrivals_terminal = models.TextField()
    term_or_con = models.TextField()
    
    
    
    

    class Meta:
        
        db_table = 'YYZ'


class DjangoMigrations(AirportMixin, models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        
        db_table = 'django_migrations'
