class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # Initially assume all three character types are missing: lowercase, uppercase, and digit.
        missing_char_types = 3
        
        # Check if the password contains at least one lowercase letter.
        if any('a' <= char <= 'z' for char in password):
            missing_char_types -= 1
        
        # Check if the password contains at least one uppercase letter.
        if any('A' <= char <= 'Z' for char in password):
            missing_char_types -= 1
        
        # Check if the password contains at least one digit.
        if any(char.isdigit() for char in password):
            missing_char_types -= 1

        # `replace_count` tracks the number of replacements needed for sequences of three or more repeating characters.
        replace_count = 0
        
        # Track sequences by their remainder when divided by 3.
        reduce_by_one = 0   # Tracks sequences where length % 3 == 0
        reduce_by_two = 0   # Tracks sequences where length % 3 == 1
        reduce_by_three = 0 # Tracks sequences where length % 3 == 2
        
        # Start scanning the password from the third character (index 2).
        index = 2
        while index < len(password):
            if password[index] == password[index-1] == password[index-2]:
                # Found a sequence of three or more repeating characters.
                repeating_length = 2
                
                # Determine the full length of this repeating sequence.
                while index < len(password) and password[index] == password[index-1]:
                    repeating_length += 1
                    index += 1
                    
                # Calculate how many replacements are needed to break up this sequence.
                replace_count += repeating_length // 3
                
                # Classify the sequence based on length % 3 to optimize future deletions.
                if repeating_length % 3 == 0:
                    reduce_by_one += 1
                elif repeating_length % 3 == 1:
                    reduce_by_two += 1
                elif repeating_length % 3 == 2:
                    reduce_by_three += 1
            else:
                # Move to the next character if no repetition.
                index += 1
        
        # Case 1: If the password is shorter than 6 characters, calculate needed insertions.
        if len(password) < 6:
            return max(missing_char_types, 6 - len(password))
        
        # Case 2: If the password length is between 6 and 20 characters, calculate replacements.
        elif len(password) <= 20:
            return max(missing_char_types, replace_count)
        
        # Case 3: If the password is longer than 20 characters, calculate deletions.
        else:
            deletions_needed = len(password) - 20  # Number of deletions to reduce length to 20.
            
            # Optimize the number of replacements by deleting characters in certain repeating sequences.

            # prioritize sequences where length % 3 == 0 (remove 1 character)
            replace_count -= min(deletions_needed, reduce_by_one)

            # sequences where length % 3 == 1 (remove 2 characters)
            replace_count -= min(max(deletions_needed - reduce_by_one, 0), reduce_by_two * 2) // 2

            # if there are still deletions left, then we can remove the need of replacements by deleting triplets
            # this also addresses the case where length % 3 == 2 (remove 3 characters)
            replace_count -= max(deletions_needed - reduce_by_one - 2 * reduce_by_two, 0) // 3 
                
            # Total steps are the sum of deletions and the maximum of remaining replacements or missing character types.
            return deletions_needed + max(missing_char_types, replace_count)