# godaddy-dynamic-dns-updater

A simple script to regularly update your DNS zone hosted at GoDaddy.com
with a dynamic IP.

## Configuration

`cp gddu.conf.example /etc/gddu.conf`

Then, edit /etc/gddu.conf and add your API key and secret. You can obtain
your keys and secrets here: https://developer.godaddy.com/keys/

## Add a cron job

To keep your IP regularly updated, you'll probably need to schedule this
script as a cron job.

You can: 
`cp gddu.py /usr/local/bin`
`cp etc/cron.d/gddu /etc/cron.d`

## Questions?

If you have any questions, feel free to reach me directly at shatlovsky@gmail.com

