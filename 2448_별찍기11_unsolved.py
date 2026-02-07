#                        *     별 1개                   
#                       * *       별1 공백1 별1             
#                      *****             별 5   
#                     *     *              별 1 공백 5 별 1     
#                    * *   * *           별1 공백1 공백3 별1 공백1 별1
#                   ***** *****                   
#                  *           *                  
#                 * *         * *                 
#                *****       *****                
#               *     *     *     *               
#              * *   * *   * *   * *              
#             ***** ***** ***** *****             
#            *                       *       첫 소거의 층은 N//2 + 1     
#           * *                     * *           
#          *****                   *****          
#         *     *                 *     *         
#        * *   * *               * *   * *        
#       ***** *****             ***** *****       
#      *           *           *           *      
#     * *         * *         * *         * *     
#    *****       *****       *****       *****    
#   *     *     *     *     *     *     *     *   
#  * *   * *   * *   * *   * *   * *   * *   * *  
# ***** ***** ***** ***** ***** ***** ***** *****


N = int(input())
star = []
for i in range(N):
    tmp_star = []
    for j in range(N-i-1):
        tmp_star.append(" ")
    for j in range(2*i+1):
        tmp_star.append("*")
    for j in range(N-i-1):
        tmp_star.append(" ")
    star.append(tmp_star)

#처리
for i in range(N//2,N):
    for j in range(N-i-1):
        star[i][j] = ' '
    
    




for row in star:
    for i in row:
        print(i,end='')
    print()
