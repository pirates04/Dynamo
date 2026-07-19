Analyze the Apache-style access log located at /app/access.log and generate a JSON summary report.

Save your findings to a file named /app/report.json. The JSON object must contain the following keys:
1. "total_requests": The total number of request entries in the access log.
2. "unique_ips": The count of unique client IP addresses.
3. "top_path": The most frequently requested URL path.

Success Criteria:
1. The output file /app/report.json must exist and contain valid JSON.
2. The "total_requests" key must correctly specify the total number of requests.
3. The "unique_ips" key must correctly count the unique IP addresses.
4. The "top_path" key must correctly identify the most frequently requested path.
