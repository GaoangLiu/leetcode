
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left = nil
    @right = nil
  end
end

# @param {TreeNode} root
# @return {Boolean}
def is_symmetric(root)
  return true if root.nil?
  mirror = lambda do |a, b|
    return true if a.nil? && b.nil?
    return false if a.nil? ^ b.nil? || a.val != b.val
    mirror.call(a.left, b.right) && mirror.call(a.right, b.left)
  end
  mirror.call(root.left, root.right)
end
