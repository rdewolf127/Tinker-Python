import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)


enrollments = read_csv('enrollments.csv')
submissions = read_csv('project_submissions.csv')
engagement = read_csv('daily_engagement.csv')


print enrollments[0]
print submissions[0]
print engagement[0]

    
