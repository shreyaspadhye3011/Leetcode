class CountWord
    def count_word_occurence(str, word)
        if (str.is_a?(String) && word.is_a?(String))
            str.count_word(word)
        else
            puts "Both parameters should be string"
        end
    end
end

class String
    def count_word(word)
        # puts self + " ~ " + word
        # puts /am/ =~ self
        # puts /\${word}/ =~ self
        # puts self.scan(word)
    end
end

# Test
CountWord.new.count_word_occurence("I am", "am")