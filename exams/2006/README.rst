2006 m. valstybinio brandos egzamino užduotis
#############################################

I. TESTAS
=========

13. Kuriai ciklo sąlygai esant bus spausdinamas skaičius ``8``? Pažymėkite teisingą atsakymą. 

    Pascal:
    
    .. code-block:: pascal
    
      program Te1; 
      var  n, k : integer; 
      begin 
          n := 2; k := 3; 
          while ??? do 
              begin 
                  k := k + 2; 
                  n := 2 * n; 
              end; 
          Write(n); 
      end. 
    
    Python:
    
    .. code-block:: python
    
      n = 2
      k = 3
      while ???:
          k = k + 2
          n = 2 * n
      print(n)
    
    ===== ==========
    **A** ``k < 10``
    **B** ``n < k``
    **C** ``k < n``
    **D** ``n < 10``
    ===== ==========

14. Kokias reikšmes įgis kintamieji ``n`` ir ``k``, į vykdžius  programą
    ``Te2``?  Pažymė kite teisingą atsakymą. 

    Pascal:
    
    .. code-block:: pascal
    
      program Te2; 
      var n, k : integer; 
      begin 
          n := 4; k := 2; 
          while (n < 10) or (k < n) do 
              begin 
                  n := 2 * k; 
                  k := 2 * n; 
              end; 
      end. 
    
    Python:
    
    .. code-block:: python
    
      n = 4
      k = 2
      while n < 10 or k < n:
          n = 2 * k
          k = 2 * n

    ===== ========= ======
          **t**     **n**
    ===== ========= ======
    **A** ``4``     ``8``
    **B** ``32``    ``16``
    **C** ``16``    ``32``
    **D** ``8``     ``4``
    ===== ========= ======

15. Kokias reikšmes įgis kintamieji ``t`` ir ``n`` įvykdžius programą ``Te3``?
    Pažymėkite teising ąatsakymą. 

    Pascal:
    
    .. code-block:: pascal
    
      program Te3; 
      var n, k : integer; 
          t : boolean; 
      begin 
          t := TRUE; n := 13; 
          for k := 5 to 8 do 
              begin 
                  if t then n := n + k 
                       else n := n - k; 
                  t := not t; 
              end; 
      end. 
    
    Python:
    
    .. code-block:: python
    
      t, n = True, 13
      for k in range(5, 9):
          n += k if t else -k
          t = not t

    ===== ========= ======
          **t**     **n**
    ===== ========= ======
    **A** ``True``  ``19``
    **B** ``True``  ``11``
    **C** ``False`` ``19``
    **D** ``False`` ``11``
    ===== ========= ======

16. Pažymėkite atsakymą, kuris būtų gautas įvykdžius programą ``Te4``. 


    Pascal:
    
    .. code-block:: pascal

      program Te4; 
      type TMas = array[1..3] of integer; 
      var A : TMas; n : integer; 
          i : integer; 
      begin 
        n := 3;  A[1] := 13; 
        for i := 2 to n do 
            if i mod 2 = 0 
                 then A[i] := A[i-1] + i 
                 else A[i] := 2 * A[i-1]; 
      end. 

    Python:
    
    .. code-block:: python

      n = 4
      A = [0, 13, 0, 0]
      for i in range(2, n):
          if i % 2 == 0:
              A[i] = A[i - 1] + i
          else:
              A[i] = 2 * A[i - 1]

    ===== ======== ======== ========
          **A[1]** **A[2]** **A[3]**
    ===== ======== ======== ========
    **A** 13       26       28
    **B** 13       28       30
    **C** 13       14       28
    **D** 13       15       30
    ===== ======== ======== ========

17. Pažymėkite atsakymą, kuris būtų gautas įvykdžius programą ``Te5``. 

    Pascal:
    
    .. code-block:: pascal

      program Te5; 
      {-------------------------------------------------} 
      procedure Pakeisti(var x : integer; y : integer); 
      begin 
          y := (x + y) * 2; 
          x := x + y; 
      end; 
      {-------------------------------------------------} 
      var a, b : integer; 
      begin 
          a := 4;  b := 2; 
          Pakeisti(a, b); 
          Pakeisti(b, a); 
          Pakeisti(a, a + b); 
          Write(a, '   ', b); 
      end. 


    Python:
    
    .. code-block:: python

      def pakeisti(x, y):
          y = (x + y) * 2
          return x + y

      a, b = 4, 2
      a = pakeisti(a, b)
      b = pakeisti(b, a)
      a = pakeisti(a, a + b)
      print(a, b, sep='   ')

    ===== =============
    **A** ``864   748``
    **B** ``416   124``
    **C** ``156   38``
    **D** ``4   2``
    ===== =============

18. Pažymėkite atsakymą, kuris būtų gautas įvykdžius programą ``Te6``, jeigu
    tekstiniame faile ``Te6.txt`` užrašyta tokia skaičių eilutė: ``13  16  -5 9
    4``

    Pascal:
    
    .. code-block:: pascal

      program Te6; 
      var a, b, c, d : integer; 
          t : boolean; 
          F : text; 
      begin 
          Assign(F, 'Te6.txt'); Reset(F); 
          Read(F, a, b); 
          t := a > b; 
          if t then Read(F, c, d, a) 
               else Read(F, a, c, d); 
          Write(a:4, b:4, c:4, d:4, t:8); 
          Close(F); 
      end. 

    Python:
    
    .. code-block:: python

      from itertools import islice
      with open('Te6.txt') as f:
          n = map(int, f.read().split())
      a, b = islice(n, 2)
      t = a > b
      if t:
          c, d, a = islice(n, 3)
      else:
          a, c, d = islice(n, 3)
      print(f'{a:4} {b:4} {c:4} {d:4} {t!r:>8}')

    ===== ===========================
    **A** ``-5  16   9   4    False``
    **B** ``13  16  -9   9     True``
    **C** ``-5  16   9   4     True``
    **D** ``13  16  -5   9    False``
    ===== ===========================
