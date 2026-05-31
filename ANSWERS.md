1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
Enhetstest:  
Testar en enskild funktion eller metod isolerat från resten av systemet. Syftet är att säkerställa att varje liten del fungerar korrekt.

Integrationstest:  
Testar hur flera delar av systemet fungerar tillsammans. Fokus ligger på samspelet mellan moduler, klasser eller komponenter.

Regressionstest:  
Testar att tidigare fungerande funktionalitet fortfarande fungerar efter ändringar i koden. Målet är att upptäcka om något gått sönder av misstag.

Prestandatest:  
Mäter hur snabbt, stabilt och resurseffektivt systemet är under belastning. Används för att hitta flaskhalsar och kapacitetsproblem.

2. Beskriv hur det går till när man arbetar med TDD.
TDD följer en återkommande cykel i tre steg:

Red – skriv ett test som misslyckas.

Green – implementera minsta möjliga kod som gör testet grönt.

Refactor – förbättra koden utan att ändra beteendet.

Denna cykel upprepas för varje liten del av funktionaliteten tills hela systemet är byggt.

3. Beskriv hur BDD skiljer sig från TDD.
TDD fokuserar på utvecklarens perspektiv och testar kodens funktioner med enhetstester.

BDD fokuserar på användarens beteende och beskriver funktionalitet i naturligt språk (Given/When/Then).

BDD används ofta för att testa hela användarflöden och säkerställa att systemet beter sig som användaren förväntar sig.

4. Vilka tester skulle du använda för en webbsida som liknar Läslistan? Motivera ditt val.
För en webbsida med både frontend och backend skulle jag använda:

Enhetstester för backend‑logik (t.ex. lägga till bok, favoritmarkering).
Motivering: Säkerställer att varje funktion fungerar isolerat.

Integrationstester för att kontrollera att backend‑delarna fungerar tillsammans.
Motivering: Upptäcker fel i samspelet mellan klasser och moduler.

End‑to‑end‑tester (Playwright/Behave) för att testa hela användarflöden i webbsidan.
Motivering: Verifierar att användaren faktiskt kan göra det som user stories beskriver.

Regressionstester för att säkerställa att nya ändringar inte förstör befintlig funktionalitet.
Motivering: Viktigt när projektet växer.

Tillsammans ger dessa tester både stabilitet, kvalitet och trygghet i utvecklingen.