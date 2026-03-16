#include <stdlib.h>
#include <string.h>

void backtrack(int row, int n, int* cols, int* diag1, int* diag2, char** board, 
               char**** res, int* returnSize) {
    if (row == n) {
        // Solution found: Resize results array and copy the current board
        *res = realloc(*res, sizeof(char**) * (*returnSize + 1));
        (*res)[*returnSize] = malloc(sizeof(char*) * n);
        for (int i = 0; i < n; i++) {
            (*res)[*returnSize][i] = strdup(board[i]);
        }
        (*returnSize)++;
        return;
    }

    for (int col = 0; col < n; col++) {
        // diag1: row - col (offset by n); diag2: row + col
        if (cols[col] || diag1[row - col + n] || diag2[row + col]) continue;

        // Place Queen
        board[row][col] = 'Q';
        cols[col] = diag1[row - col + n] = diag2[row + col] = 1;

        backtrack(row + 1, n, cols, diag1, diag2, board, res, returnSize);

        // Backtrack: Remove Queen
        board[row][col] = '.';
        cols[col] = diag1[row - col + n] = diag2[row + col] = 0;
    }
}

char*** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {
    *returnSize = 0;
    char*** res = NULL;
    
    // 1. Initialize temporary working board
    char** board = malloc(sizeof(char*) * n);
    for (int i = 0; i < n; i++) {
        board[i] = malloc(n + 1);
        memset(board[i], '.', n);
        board[i][n] = '\0';
    }

    // 2. Lookup arrays for O(1) safety checks
    int* cols = calloc(n, sizeof(int));
    int* diag1 = calloc(2 * n, sizeof(int)); // row - col
    int* diag2 = calloc(2 * n, sizeof(int)); // row + col

    // 3. Start recursive backtracking
    backtrack(0, n, cols, diag1, diag2, board, &res, returnSize);

    // 4. Fill returnColumnSizes (Each solution has 'n' rows)
    *returnColumnSizes = malloc(sizeof(int) * (*returnSize));
    for (int i = 0; i < *returnSize; i++) {
        (*returnColumnSizes)[i] = n;
    }

    // 5. Clean up temporary memory
    for (int i = 0; i < n; i++) free(board[i]);
    free(board);
    free(cols);
    free(diag1);
    free(diag2);

    return res;
}
