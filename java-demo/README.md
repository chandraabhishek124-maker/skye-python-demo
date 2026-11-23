# Java Example Domain demo

Requires JDK 11 or later, Maven and Chrome with its required system libraries.
From this directory, run `mvn -B test`. Chrome runs headless by default;
set the environment variable `HEADLESS=0` for a visible browser.

The test verifies the page title, English description and Learn more link.
TestNG reports are written to `target/surefire-reports/`.

For Skye's general From Repo suite, select the Java with chrome image and
use this inline Run Config YAML from the repository root:

```yaml
runnertag: "1.0.0"
steps:
  - name: "Check Java and Maven"
    commands:
      - java -version
      - mvn -version
  - name: "Run Java Example Domain test"
    commands:
      - mvn -B -f java-demo/pom.xml test
```

Maven dependencies and matching browser-driver downloads need network access.
The runner image must provide a compatible JDK and Chrome. A pod startup
failure occurs before this test executes and requires runner investigation.
