Feature: Avmarkera en favoritbok
  Som en användare
  Vill jag kunna ta bort en bok från mina favoriter
  Så att min favoritlista hålls uppdaterad

Scenario: Användaren avmarkerar en favoritbok
  Given att användaren öppnar webbsidan
  And att användaren har en favoritbok
  When användaren avmarkerar boken som favorit
  Then ska boken inte längre visas i favoritlistan
