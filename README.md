**Mikołaj Mentel**

# **1.Wstęp**
Mikołaj Mentel - rekrutacja OpenX
Zadanie - Wariant 1

Założyłem, że srednią wartosc i medianę mamy policzyć dla poddrzewa danego wezla. 
Nie do końca zrozumiałem czy wymagany jest osobny obiekt ze zdefiniowanymi metodami do obliczania
średniej, mediany i sumy, czy może byc to wywoływane na obiektach node. Działanie tych metod i tak
by sie zbytnio nie rożniło (zamiast self po prostu podawalibyśmy węzeł jako argument) więc wybrałem
opcję ktora wydawała mi się bardziej odpowiednia.

Co do klasy Node, zamiast pól children i maxChildren, klasa mogłaby mieć po prostu leftChild, rightChild,
ale to co będzie bardziej praktyczne zależy od tego w jaki sposób będzie ta klasa używana. Nie ma zaznaczonego
że drzewo zawsze musi byc binarne i przy większej ilości dzieci wystarczy zmienić pole maxChildren, a reszta nadal
będzie działać poprawnie.

# **2.Implementacja**

- ```class Node:```

Klasa reprezentująca wierzchołek drzewa, której używamy do stworzenia struktury drzewa.
Drzewo reprezentowane jest przez listę wskaźnikową. Każdy węzeł ma wartość i tablicę przechowującą
referencję do jego dzieci.


- ```def __init__(self, value):```

Konstruktor tworzący objekt klasy Node. Za argument pobiera value, które ustawiane jest jako wartość danego węzła. 
Konstruktor sprawdza czy value jest typu int, jeśli nie podnosi TypeError. Ustawia również maksymalną ilość dzieci na 2
i tworzy pustą listę dzieci. 

- ```def add_child(self, child):```

Funkcja służąca do dodawania dzieci węzła. Child może być zarówno obiektem klasy Node, jak i intem. Jeśli jest
czymś innym, podnoszony jest TypeError. Dzieci dodajemy od lewej strony. Jeśli węzeł ma już maksymalną ilość dzieci,
podnoszony jest wyjątek ValueError. 

- ```def subtree_sum(self):```

Funkcja do liczenia sumy wartości w poddrzewie. Funkcja rekurencyjnie sumuje wartości kolejnych potomków aż w końcu, 
zwróci ją do korzenia który ją zwraca.

- ```def count_descendants(self):```

Funkcja licząca ilość potomków danego węzła. Wykorzystywana do liczenia średniej. Można by ją zastąpić poprzez użycie
get_descendants i .sum / len() ale zależy od wymagań. 

- ```def subtree_average(self):```

Funkcja licząca średnią arytmetyczną wartości w poddrzewie. Funkcja wywołuje subtree_sum() i dzieli wynik przez 
count_descendants()

- ```def get_descendants(self):```

Funkcja zwracająca listę wartości potomków. Wykorzystywana do liczenia mediany. 

- ```def subtree_median(self):```

Funkcja licząca medianę wartości w poddrzewie. Funkcja wywołuję get_descendants aby dostać listę potomków, 
następnie sortuję wartości przy pomocy .sort() (złożoność O(n*logn) więc identyczne jak quicksort). W sumie przez fakt, 
że najpierw musimy stworzyć tablicę potomków mamy złożoność O(n+n*logn) a to w efekcie i tak pozostaje jako O(n*logn).
Dla małych drzew (poniżej bodajże 4 wierzchołków, mogłoby być lepsze użycie mergesorta, czyli zamiast najpierw tworzyć
a potem sortować listę, od razu łączylibyśmy rekurencyjnie posortowane listy, jednak .sort() i tak mógłby wypaść 
lepiej). Gdy tablica jest posortowana to sprawdzamy czy jej długość jest parzysta czy nie i liczymy odpowiednio medianę.

- ```def __str__(self, level=0):```

Funkcja do reprezentacji drzewa jako stringa. Przydatna przy testach i debugowaniu.

- ```def parser(array):```

Funkcja do parsowania drzewa z listy. Dla dużych drzew niewygodne by było pisać node.node.node.node aby dodać nowego 
node'a więc używam parsera który przyjmuję jako argument listę. W liście tej każdy node jest reprezentowany jako lista,
w której pierwszy element to jego wartość, a kolejne to jego dzieci. Przykładowo, drzewo z polecenia można przedstawić
jako [5, [3, [2], [5]], [7, [1], [0, [2], [8, [5]]]]]. Zwraca korzeń drzewa. 

# **3.Testy**

Testy wykorzystujące klasę unittest. 

- ```testTrees```

Lista drzew dla których uruchomione zostaną testy ```test_str```, ```test_subtree_average```, ```test_subtree_median```
i ```test_subtree_sum```.

- ```averageTestCases```

Oczekiwane wyniki dla liczenia średniej

- ```medianTestCases```

Oczekiwane wyniki dla liczenia mediany

- ```sumTestCases```

Oczekiwane wyniki dla liczenia sumy

- ```strTestCases```

Oczekiwane wyniki dla funkcji str()

# **4.Koniec**
Pewnie nikt nie dotrwa żeby to czytać ale przypominam, że myjemy rondżgi
 
 /╲/\╭( ͡° ͡° ͜ʖ ͡° ͡°)╮/\╱\
 
 Serdecznie pozdrawiam i życzę miłego siedzenia w domku.

