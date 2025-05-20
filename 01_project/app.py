import streamlit as st
import random

def advanced_number_guessing_game():
    st.title("🎯 Advanced Number Guessing Game")
    
    # Difficulty selection
    difficulty = st.radio("Select difficulty:", 
                         ["Easy (1-50)", "Medium (1-100)", "Hard (1-200)"], 
                         index=1)
    
    # Set range based on difficulty
    if difficulty == "Easy (1-50)":
        max_num = 50
    elif difficulty == "Medium (1-100)":
        max_num = 100
    else:
        max_num = 200
    
    # Initialize game state
    if 'target_number' not in st.session_state or st.session_state.max_num != max_num:
        st.session_state.target_number = random.randint(1, max_num)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.session_state.max_num = max_num
        st.session_state.guesses = []
    
    # Display instructions
    st.write(f"I'm thinking of a number between 1 and {max_num}. Can you guess it?")
    
    # Gameplay section - only show if game isn't over
    if not st.session_state.game_over:
        # Input for user's guess
        guess = st.number_input("Enter your guess:", min_value=1, max_value=max_num, step=1)
        
        # Check guess button
        if st.button("Check Guess"):
            st.session_state.attempts += 1
            st.session_state.guesses.append(guess)
            
            if guess < st.session_state.target_number:
                st.warning("Too low! Try a higher number.")
            elif guess > st.session_state.target_number:
                st.warning("Too high! Try a lower number.")
            else:
                st.session_state.game_over = True
    
    # Congratulation message when game is won
    if st.session_state.game_over:
        st.success(f"🎉 Congratulations! You guessed the number {st.session_state.target_number} in {st.session_state.attempts} attempts!")
        st.balloons()
        
        # Display all guesses
        st.write("Your guess history:", st.session_state.guesses)
        
        # Restart options
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🎮 Play Again (Same Difficulty)"):
                st.session_state.target_number = random.randint(1, max_num)
                st.session_state.attempts = 0
                st.session_state.game_over = False
                st.session_state.guesses = []
                st.rerun()
        with col2:
            if st.button("🔄 Change Difficulty & Restart"):
                st.session_state.target_number = random.randint(1, max_num)
                st.session_state.attempts = 0
                st.session_state.game_over = False
                st.session_state.guesses = []
                st.session_state.max_num = max_num  # This will be updated by difficulty change
                st.rerun()
    
    # Show previous guesses during gameplay
    if not st.session_state.game_over and st.session_state.attempts > 0:
        st.write("Your guesses so far:", st.session_state.guesses)

if __name__ == "__main__":
    advanced_number_guessing_game()