# Archived
This repository was archived following SquareSoft's acquisition of google domains as detailed in [Google's FAQ](https://support.google.com/domains/answer/13689670?hl=en)


# dynamic_dns
Update google domains dns records.

create image by using the command
> docker image build -t dynamic_dns:latest .

deploy yaml
> docker stack deploy dyncont -c dynamic_dns.yaml
