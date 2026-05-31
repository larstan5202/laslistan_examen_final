Feature: Lägga till en ny bok
  Som en användare
  Vill jag kunna lägga till en ny bok i katalogen
  Så att jag kan utöka listan med böcker

  Scenario: Användaren lägger till en ny bok
    Given att användaren öppnar webbsidan
    When användaren lägger till en ny bok med författare "Testförfattare" och titel "Testtitel"
    Then ska den nya boken visas i katalogen
