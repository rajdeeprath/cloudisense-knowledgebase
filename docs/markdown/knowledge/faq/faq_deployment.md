## Deployment & Installation

### ❓ How do I install CloudiSENSE on Ubuntu?
**Answer:**  
You can install CloudiSENSE on Ubuntu in two ways:

1. **Using the installer script:**  
   - Visit: [CloudiSENSE Installer](https://github.com/rajdeeprath/cloudisense-installer)
   - Follow the instructions to run the automated installer script.

2. **Using Docker:**  
   - Visit: [CloudiSENSE Docker Deployment](https://github.com/rajdeeprath/cloudisense-docker)
   - Use Docker to quickly set up and run CloudiSENSE in a containerized environment.

For any additional help or installation issues, you can contact the developer directly.


### ❓ Can I run CloudiSENSE inside Docker?
**Answer:**  
Yes, CloudiSENSE can be easily run inside a Docker container.

A pre-configured Docker deployment is available here:  
[CloudiSENSE Docker Deployment](https://github.com/rajdeeprath/cloudisense-docker)

This setup allows you to:
- Run CloudiSENSE without installing it directly on the host system.
- Manage dependencies and environment configuration easily.
- Deploy CloudiSENSE consistently across different environments.

For detailed instructions, refer to the repository or contact the developer if you need assistance.


### ❓ How do I deploy CloudiSENSE on AWS EC2?
**Answer:**  
You can deploy CloudiSENSE on AWS EC2 easily by following these steps:

1. **Launch an EC2 Instance:**  
   - Choose an Ubuntu-based AMI (Amazon Machine Image).
   - Select an appropriate instance type (e.g., t2.medium or higher for production).

2. **Setup the Server:**  
   - Connect to the instance via SSH.
   - Update the system packages.

3. **Install CloudiSENSE:**  
   - Use the installer script:  
     [CloudiSENSE Installer](https://github.com/rajdeeprath/cloudisense-installer)

4. **Configure Security Groups:**  
   - Open required ports (default: 8000 for HTTP, 8080 for HTTPS).
   - Ensure outbound connections are allowed for external communications.

5. **Access the Service:**  
   - Access the CloudiSENSE UI from your browser using the EC2 public IP and appropriate port.

---

**Alternatively, use Docker:**  
- You can also deploy CloudiSENSE quickly using Docker.  
- Use the official Docker setup:  
  [CloudiSENSE Docker Deployment](https://github.com/rajdeeprath/cloudisense-docker)

---

For detailed deployment assistance or production optimization, you can contact the developer.


### ❓ What is the recommended system configuration?
**Answer:**  
For running CloudiSENSE efficiently, the recommended minimum system configuration is:

- **Operating System:**  
  Debian-based or RedHat-based Linux distribution (must support Python 3)

- **CPU:**  
  Dual-core processor or higher (≥ 2 vCPUs recommended)

- **RAM:**  
  At least 256 MB (higher recommended for production environments)

- **Memory Usage:**  
  Typically around 30–40 MB (can increase based on active modules and libraries)

- **CPU Usage:**  
  Typically around 2–5% during normal operation

---

CloudiSENSE is designed to be lightweight and optimized, making it suitable even for small servers, cloud VMs, and edge devices.


### ❓ How do I perform an offline installation?
**Answer:**  
Coming soon.

