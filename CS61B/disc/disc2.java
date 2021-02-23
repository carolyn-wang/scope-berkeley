public static void fillGrid(int[] LL, int[] UR, int[][] S){
    int N = S.length;
    int kL, int kR;
    kL,kR = 0;
    for (int i=0 ; i < n; i++){
        for (int j = 0; j<= n; j++){
            if (i<j){
                S[i][j] = UR[kR];
                kR++;

            }
            else if (i>j){
                S[i][j] = LL[kL);
                kL++;
            }
        }
    }

public static IntList[] partition(IntList lst, int k) {
    IntList[] array = new IntList[k];
    int index = 0;
    IntList L = lst.reverse();
    while (L != null) {
        array[k].insert(L.first);

    if (L.length() % (k-1) <= 1){
        k--;
    }

    index = (index + 1 ) % array.length;
}
return array;
}