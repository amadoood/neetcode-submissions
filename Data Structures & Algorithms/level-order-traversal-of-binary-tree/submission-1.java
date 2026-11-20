/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
//import java.util.ArrayDeque;
//import java.util.Queue;

class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        List<Integer> currentLevel = new ArrayList<>();
        currentLevel.add(root.val);
        result.add(currentLevel);
        
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while(!queue.isEmpty()) {
            currentLevel = new ArrayList<>();
            int currentSize = queue.size();

            for(int i = 0; i < currentSize; i++) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                    currentLevel.add(node.left.val);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                    currentLevel.add(node.right.val);
                }
            }
            if(!currentLevel.isEmpty()) result.add(currentLevel);
        }

        return result;
        
    }
}
