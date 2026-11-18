# Exercise 3: HTTP Security Header Analysis

# Objective
To inspect and analyse HTTP response headers of OWASP Juice Shop using Burp Suite and identify security-related headers.

# Tools Used
- Burp Suite Community Edition
- OWASP Juice Shop
- Web Browser

# Steps Performed
1. Started OWASP Juice Shop on localhost.
2. Opened Burp Suite and navigated to Proxy → HTTP history.
3. Selected the GET request for the application's root page.
4. Inspected the HTTP response headers.
5. Identified security-related headers and examined their purpose.

# Results

The server returned `HTTP/1.1 200 OK`.

The following security-related headers were observed:

|           Header            |      Value     |
|-----------------------------|----------------|
| Access-Control-Allow-Origin |        *       |
| X-Content-Type-Options      | nosniff        |
| X-Frame-Options             | SAMEORIGIN     |
| Feature-Policy              | payment 'self' |

Additional observations:
- `X-Content-Type-Options: nosniff` helps prevent MIME-type sniffing.
- `X-Frame-Options: SAMEORIGIN` restricts cross-origin framing.
- `Access-Control-Allow-Origin: *` allows cross-origin access, subject to CORS restrictions.
- Content-Security-Policy, Strict-Transport-Security and Referrer-Policy were not visible in this response.

# Conclusion
The HTTP response headers were successfully inspected using Burp Suite. The analysis identified existing security headers and configurations requiring further investigation. The findings provide a starting point for assessing the application's HTTP security configuration.