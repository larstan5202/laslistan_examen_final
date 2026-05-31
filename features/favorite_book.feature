Feature: Markera en bok som favorit
  Som en användare
  Vill jag kunna markera en bok som favorit
  Så att jag kan spara böcker jag gillar

  Scenario: Användaren markerar en bok som favorit
    Given att användaren öppnar webbsidan
    When användaren markerar första boken som favorit
    Then ska boken visas i favoritlistan
