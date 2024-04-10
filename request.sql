SELECT
  MIN(temperatur) AS min_temperatur,
  MAX(temperatur) AS max_temperatur,
  AVG(temperatur) AS durchschnittliche_temperatur
FROM feinstaub.DHT22
WHERE zeitstempel like '2022-03-14%';
