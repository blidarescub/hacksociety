from django.core.management.base import BaseCommand, CommandError
from gov_api.models import Entry
import csv


class Command(BaseCommand):
    help = 'Upload CSV data from file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fisier',
            action='store',
            dest='fisier',
            required=True,
            help='Fisierul CSV in formatul standard.',
        )

        parser.add_argument(
            '--anul',
            dest='anul',
            required=True,
            help='Anul pentru care se uploadeaza datele.',
        )

    def handle(self, *args, **options):
        with open(options['fisier'], 'r') as fisier:
            parser = csv.reader(fisier)
            cap_tabel = parser.next()

            for row in parser:
                try:
                    entry = Entry.objects.create(
                        cod_unic_candidat=row[0],
                        sex=row[1],
                        specializare=row[2],
                        profil=row[3],
                        fileira=row[4],
                        forma_de_invatamant=row[5],
                        mediu_candidat=row[6],
                        unitate_siiir=row[7],
                        unitate_sirues=row[8],
                        clasa=row[9],
                        subiect_ea=row[10],
                        subiect_eb=row[11],
                        limba_moderna=row[12],
                        subiect_ec=row[13],
                        subiect_ed=row[14],
                        promotie=row[15],
                        note_recun_a=row[16],
                        note_recun_b=row[17],
                        note_recun_c=row[18],
                        note_recun_d=row[19],
                        note_recun_ea=row[20],
                        note_recun_eb=row[21],
                        note_recun_ec=row[22],
                        note_recun_ed=row[23],
                        status_a=row[24],
                        status_b=row[25],
                        status_c=row[26],
                        status_d=row[27],
                        status_ea=row[28],
                        status_eb=row[29],
                        status_ec=row[30],
                        status_ed=row[31],
                        ita=row[32],
                        scris_itc=row[33],
                        scris_pms=row[34],
                        oral_pmo=row[35],
                        oral_io=row[36],
                        nota_ea=row[37],
                        nota_eb=row[38],
                        nota_ec=row[39],
                        nota_ed=row[40],
                        contestatie_ea=row[41],
                        nota_contestatie_ea=row[42],
                        contestatie_eb=row[43],
                        nota_contestatie_eb=row[44],
                        contestatie_ec=row[45],
                        nota_contestatie_ec=row[46],
                        contestatie_ed=row[47],
                        nota_contestatie_ed=row[48],
                        punctaj_digitale=row[49],
                        status=row[50],
                        medie=row[51],
                        anul=options['anul']
                    )
                    self.stdout.write(self.style.SUCCESS('Uploaded student "%s"' % entry.cod_unic_candidat))
                except Exception, e:
                    raise CommandError('%s' % e)

            self.stdout.write(self.style.SUCCESS('Successfully uploaded data from "%s"' % fisier))
