from __future__ import unicode_literals

from django.db import models
import arrow


class Entry(models.Model):

    cod_unic_candidat = models.CharField(max_length=1024, blank=True, null=True, db_index=True)
    sex = models.CharField(max_length=1024, blank=True, null=True)
    specializare = models.CharField(max_length=1024, blank=True, null=True)
    profil = models.CharField(max_length=1024, blank=True, null=True)
    fileira = models.CharField(max_length=1024, blank=True, null=True)
    forma_de_invatamant = models.CharField(max_length=1024, blank=True, null=True)
    mediu_candidat = models.CharField(max_length=1024, blank=True, null=True)
    unitate_siiir = models.CharField(max_length=1024, blank=True, null=True)
    unitate_sirues = models.CharField(max_length=1024, blank=True, null=True)
    clasa = models.CharField(max_length=1024, blank=True, null=True)
    subiect_ea = models.CharField(max_length=1024, blank=True, null=True)
    subiect_eb = models.CharField(max_length=1024, blank=True, null=True)
    limba_moderna = models.CharField(max_length=1024, blank=True, null=True)
    subiect_ec = models.CharField(max_length=1024, blank=True, null=True)
    subiect_ed = models.CharField(max_length=1024, blank=True, null=True)
    promotie = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_a = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_b = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_c = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_d = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_ea = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_eb = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_ec = models.CharField(max_length=1024, blank=True, null=True)
    note_recun_ed = models.CharField(max_length=1024, blank=True, null=True)
    status_a = models.CharField(max_length=1024, blank=True, null=True)
    status_b = models.CharField(max_length=1024, blank=True, null=True)
    status_c = models.CharField(max_length=1024, blank=True, null=True)
    status_d = models.CharField(max_length=1024, blank=True, null=True)
    status_ea = models.CharField(max_length=1024, blank=True, null=True)
    status_eb = models.CharField(max_length=1024, blank=True, null=True)
    status_ec = models.CharField(max_length=1024, blank=True, null=True)
    status_ed = models.CharField(max_length=1024, blank=True, null=True)
    ita = models.CharField(max_length=1024, blank=True, null=True)
    scris_itc = models.CharField(max_length=1024, blank=True, null=True)
    scris_pms = models.CharField(max_length=1024, blank=True, null=True)
    oral_pmo = models.CharField(max_length=1024, blank=True, null=True)
    oral_io = models.CharField(max_length=1024, blank=True, null=True)
    nota_ea = models.CharField(max_length=1024, blank=True, null=True)
    nota_eb = models.CharField(max_length=1024, blank=True, null=True)
    nota_ec = models.CharField(max_length=1024, blank=True, null=True)
    nota_ed = models.CharField(max_length=1024, blank=True, null=True)
    contestatie_ea = models.CharField(max_length=1024, blank=True, null=True)
    nota_contestatie_ea = models.CharField(max_length=1024, blank=True, null=True)
    contestatie_eb = models.CharField(max_length=1024, blank=True, null=True)
    nota_contestatie_eb = models.CharField(max_length=1024, blank=True, null=True)
    contestatie_ec = models.CharField(max_length=1024, blank=True, null=True)
    nota_contestatie_ec = models.CharField(max_length=1024, blank=True, null=True)
    contestatie_ed = models.CharField(max_length=1024, blank=True, null=True)
    nota_contestatie_ed = models.CharField(max_length=1024, blank=True, null=True)
    punctaj_digitale = models.CharField(max_length=1024, blank=True, null=True)
    status = models.CharField(max_length=1024, blank=True, null=True)
    medie = models.CharField(max_length=1024, blank=True, null=True)
    anul = models.CharField(max_length=1024, blank=True, null=True, default=str(arrow.now().year))

    class Meta:
        verbose_name_plural = 'Entries'

    def __unicode__(self):
        if not self.cod_unic_candidat:
            return unicode(self.id)
        else:
            return unicode(self.cod_unic_candidat)
