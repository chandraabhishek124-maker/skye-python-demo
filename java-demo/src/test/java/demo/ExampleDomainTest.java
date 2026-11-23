package demo;

import java.time.Duration;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.Test;

public class ExampleDomainTest {
    @Test
    public void verifyExampleDomain() {
        ChromeOptions options = new ChromeOptions();
        if (!"0".equals(System.getenv("HEADLESS"))) {
            options.addArguments("--headless=new");
        }
        WebDriver driver = new ChromeDriver(options);
        try {
            driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(30));
            driver.get("https://example.com/");
            WebElement description = new WebDriverWait(driver, Duration.ofSeconds(15))
                .until(ExpectedConditions.visibilityOfElementLocated(
                    By.cssSelector("p[lang='en']")));
            Assert.assertEquals(driver.getTitle(), "Example Domain");
            Assert.assertTrue(description.getText().contains(
                "This domain is for use in documentation examples"));
            WebElement link = driver.findElement(By.linkText("Learn more"));
            Assert.assertTrue(link.isDisplayed());
            Assert.assertEquals(link.getAttribute("href"),
                "https://iana.org/help/example-domains");
        } finally {
            driver.quit();
        }
    }
}
