create view servidorx as
  select distinct siape as id, nome, siape from servidor order by siape;