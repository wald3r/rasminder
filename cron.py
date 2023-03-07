from crontab import CronTab

my_cron = CronTab(user='walder')

job = my_cron.new(command = 'python /home/walder/main.py')



my_cron.write()