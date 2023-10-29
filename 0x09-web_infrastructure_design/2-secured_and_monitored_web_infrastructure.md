 Secured and monitored web infrastructure




Description

This is a 3-server secured, encrypted and monitored web infrastructure.

Specifics about this infrastructure

The Load Balancer: It will be responsible for distributing incoming traffic evenly across the web server and database server to ensure that the website can handle high levels of traffic without downtime. It is also responsible for encrypting traffic, ensuring that all data transmitted between the user and the website is secure and cannot be accessed by third parties.

The Web Server: It will be responsible for hosting the website's content and serving it to users who visit the website.It will also be responsible for running any server side scripts or applications that are needed to power the website.

The Database Server: It will be responsible for storing the website’s data such as user information.It will also be responsible for providing the web server with the data it needs to generate dynamic web pages for the website.

The SSL Certificate: It will be responsible for serving the website over HTTPS, encrypting traffic between clients and the web servers. They protect data in transit, ensuring confidentiality and data integrity.

Purpose of the firewall
A firewall is a security system designed to prevent unauthorized access to and from a private network.Firewalls can be hardware-based, software-based or a combination of both.They are commonly used to protect networks from external threats like hackers and viruses.

Why is the traffic served over HTTPS 
HTTPs is a secure version of HTTP protocol, which is a tool used to transfer data over the web.When a website uses HTTPS, it means that all communication between the web server and the client’s web browser is encrypted and secure.Since HTTPS provides a secure connection, it helps to ensure the integrity of the data that is transmitted, which is crucial for ensuring that the information on a website is accurate.

Importance of monitoring 
A monitoring tool is a type of software or hardware that is used to collect data about a system, network or application.The data can be used to monitor the health and performance of the system.Monitoring tools provide valuable insights into the behavior and operation of a system and can help ensure that it is running smoothly and efficiently.Monitoring is crucial for identifying and resolving issues proactively.


What to do to Monitor a Web Server’s QPS 
To monitor web server QPS, follow the steps below:
1. Set up monitoring clients to collect data from the web servers, focusing on incoming queries and response times.
2. Configure the monitoring tool to parse and analyze the collected data.
3. Create dashboards and alerts to track and notify you of fluctuations in QPS.
4. Regularly review the QPS data to identify trends, anomalies or performance issues.Adjust server resources or optimize code as needed.

Why Terminating SSL at the Load Balancer Level is an issue:
Terminating SSL at the Load Balancer Level is a security risk. This is because data will be transmitted unencrypted between the load balancer and web servers.Attackers who have access to the segment can intercept data.

Why having only one MySQL Server capable of accepting writes is an issue:
This can create a single point of failure in your system.If the MySQL server goes down,it affects the entire system’s ability to accept and update data.To address this, it is generally best to have multiple MySQL servers that are capable of accepting writes,consider clustering, replication, or high availability solutions for the database.




Why having servers with all the same components (database, web server and application server) might be a problem:
In this case if a server’s database is compromised or goes down, it can take the rest of the system down with it.This can lead to decreased reliability and increased downtime for the system as a whole.Diversifying  components enhances security. 

