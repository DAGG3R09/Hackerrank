#https://www.hackerrank.com/challenges/tree-level-order-traversal

/*
struct node
{
    int data;
    node* left;
    node* right;
}*/

void levelOrder(node * root) {
  void levelOrder(Node root) {
   Queue<Node> q = new LinkedList<>();
   Node s;
   q.add(root);

    while(!q.isEmpty()) {
        s = q.poll();
        System.out.print(s.data+" ");
        if (s.left != null)
            q.add(s.left);
        if (s.right != null)
            q.add(s.right);

    }
 }
}
