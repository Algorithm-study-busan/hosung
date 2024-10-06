SELECT start.machine_id, ROUND(AVG(end.timestamp - start.timestamp), 3) processing_time
FROM Activity start
JOIN Activity end on start.machine_id = end.machine_id and start.process_id = end.process_id and end.activity_type = 'end' and start.activity_type = 'start'
GROUP BY start.machine_id
