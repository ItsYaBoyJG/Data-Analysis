class PasserRating:
  def __init__(self) -> None:
    pass


  def passer_rating(comp, attempts, tds, yards, inrcpts):
      return ((((comp / attempts)- 0.3) * 5) + (((yards / attempts) - 3) 
                                              * 0.25) + ((tds / attempts) * 20) 
              + (2.375 ((inrcpts / attempts) * 25))) / (6/100)  
  
  
  
      

      