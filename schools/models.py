import uuid
from django.db import models
from users.models import Profile

class School(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    urn = models.BigIntegerField(default=0, null=True, blank=True)
    la_name = models.CharField(max_length=500, null=True, blank=True)
    establishment_number = models.IntegerField(default=0, null=True, blank=True)
    establishment_name = models.CharField(max_length=500, null=True, blank=True)
    type_of_establishment = models.CharField(max_length=500, null=True, blank=True)
    establishment_type_group = models.CharField(max_length=500, null=True, blank=True)
    establishment_status = models.CharField(max_length=500, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default='default.jpg')
    phase_of_education = models.CharField(max_length=500, null=True, blank=True)
    statutory_low_age = models.IntegerField(default=0, null=True, blank=True)
    statutory_high_age = models.IntegerField(default=0, null=True, blank=True)
    boarders = models.CharField(max_length=500, null=True, blank=True)
    nursery_provision = models.CharField(max_length=500, null=True, blank=True)
    official_sixth_form = models.CharField(max_length=500, null=True, blank=True)
    gender = models.CharField(max_length=500, null=True, blank=True)
    religious_character = models.CharField(max_length=500, null=True, blank=True)
    religious_ethos = models.CharField(max_length=500, null=True, blank=True)
    admissions_policy = models.CharField(max_length=500, null=True, blank=True)
    school_capacity = models.IntegerField(default=0, null=True, blank=True)
    special_classes = models.CharField(max_length=500, null=True, blank=True)
    census_date = models.DateField(null=True, blank=True)
    number_of_pupils = models.IntegerField(default=0, null=True, blank=True)
    number_of_boys = models.IntegerField(default=0, null=True, blank=True)
    number_of_girls = models.IntegerField(default=0, null=True, blank=True)
    percentage_fsm = models.FloatField(default=0, null=True, blank=True)
    trust_school_flag = models.CharField(max_length=500, null=True, blank=True)
    school_sponsor_flag = models.CharField(max_length=500, null=True, blank=True)
    federation_flag = models.CharField(max_length=500, null=True, blank=True)
    federations = models.CharField(max_length=500, null=True, blank=True)
    ukprn = models.IntegerField(default=0, null=True, blank=True)
    ofsted_last_insp = models.DateField(null=True, blank=True)
    ofsted_special_measures = models.CharField(max_length=500, null=True, blank=True)
    last_changed_date = models.DateField(null=True, blank=True)
    street = models.CharField(max_length=500, null=True, blank=True)
    locality = models.CharField(max_length=500, null=True, blank=True)
    address3 = models.CharField(max_length=500, null=True, blank=True)
    town = models.CharField(max_length=500, null=True, blank=True)
    county = models.CharField(max_length=500, null=True, blank=True)
    postcode = models.CharField(max_length=500, null=True, blank=True)
    school_website = models.CharField(max_length=500, null=True, blank=True)
    telephone_number = models.CharField(max_length=500, null=True, blank=True)
    head_title = models.CharField(max_length=500, null=True, blank=True)
    head_first_name = models.CharField(max_length=500, null=True, blank=True)
    head_last_name = models.CharField(max_length=500, null=True, blank=True)
    head_preferred_job_title = models.CharField(max_length=500, null=True, blank=True)
    sen1 = models.CharField(max_length=500, null=True, blank=True)
    sen2 = models.CharField(max_length=500, null=True, blank=True)
    sen3 = models.CharField(max_length=500, null=True, blank=True)
    sen4 = models.CharField(max_length=500, null=True, blank=True)
    type_of_resourced_provision = models.CharField(max_length=500, null=True, blank=True)
    resourced_provision_on_roll = models.IntegerField(default=0, null=True, blank=True)
    resourced_provision_capacity = models.IntegerField(default=0, null=True, blank=True)
    sen_unit_on_roll = models.IntegerField(default=0, null=True, blank=True)
    sen_unit_capacity = models.IntegerField(default=0, null=True, blank=True)
    gor = models.CharField(max_length=500, null=True, blank=True)
    district_administrative = models.CharField(max_length=500, null=True, blank=True)
    administrative_ward = models.CharField(max_length=500, null=True, blank=True)
    parliamentary_constituency = models.CharField(max_length=500, null=True, blank=True)
    urban_rural = models.CharField(max_length=500, null=True, blank=True)
    easting = models.IntegerField(default=0, null=True, blank=True)
    northing = models.IntegerField(default=0, null=True, blank=True)
    msoa = models.CharField(max_length=500, null=True, blank=True)
    lsoa = models.CharField(max_length=500, null=True, blank=True)
    ofsted_rating = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    uprn = models.BigIntegerField(default=0, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.establishment_name if self.establishment_name else "No Name"

    class Meta:
        ordering = ['-vote_ratio', '-vote_total', 'establishment_name']

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('parent__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    parent = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)  
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['parent', 'school']]
        ordering = ['-created']