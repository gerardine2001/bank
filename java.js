class My_car{
 constructor(name,year){
     this.name=name;
     this.year=year;

    }
   age(){
       let  date=new Date();
       return date.getFullYear-this.year;
   }
}
car