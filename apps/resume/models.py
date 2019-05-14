from django.db import models

class Resume(models.Model):
    """
    A resume object that contains multiple ResumeItem
    """
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=127)

class ResumeItem(models.Model):
    """
    A single resume item, representing a job and title held over a given period
    of time.
    """
    user = models.ForeignKey('auth.User')

    jobTitle = models.CharField(max_length=127)
    company = models.CharField(max_length=127)

    start_date = models.DateField()
    # Null end date indicates position is currently held
    end_date = models.DateField(null=True, blank=True)

    description = models.TextField(max_length=2047, blank=True)

    # Using ManyToManyField so a ResumeItem can be used in many resumes
    resumes = models.ManyToManyField('Resume', related_name='items')

    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.user.username,
                                          self.jobTitle,
                                          self.company,
                                          self.start_date.isoformat())
