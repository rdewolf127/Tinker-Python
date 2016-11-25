import unicodecsv

with open('enrollments.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

enrollments[0]

with open('project_submissions.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    submissions = list(reader)

submissions[0]

with open('daily_engagement.csv', 'rb') as f:
    reader = unicodecsv.DictReader(f)
    engagement = list(reader)

engagement[0]


    