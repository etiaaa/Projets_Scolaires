public class Main {
    //Question 1
    public Main(int n) {
        this.n = n;
    }

    public static void main(String[] args){
        //Question 1:
        tableDe7(8);

    }

    //question 1
    public static void tableDe7(int n) {
        String resulat = "";
        for (int i = 1; i < n + 1; i++) {
            resulat = resulat + i * 7;
            if ((i * n) % 3 == 0) {
                resulat += "*";
            }
            resulat += " ";
        }
        System.out.println(resulat);
    }
    private int n;


    //Question 3:
    //Apres

    //Question 4:
    //Fait

    //Question 5:

}

