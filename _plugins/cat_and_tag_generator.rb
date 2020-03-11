module Jekyll

  module Slug2Filter
    def slugify_nonascii(input)
      return Utils.slugify(input).gsub(/\s/, '-').gsub(/[áàäâ]/, 'a').gsub(/[éèëê]/, 'e').gsub(/[íìïî]/, 'i').gsub(/[óòöô]/, 'o').gsub(/[úùüû]/, 'u').gsub('ñ', 'n').gsub('ç', 's')

    end
  end


  # module AssetFilter
  #   def slugify_nonascii(input)
  #     return Utils.slugify(input).gsub(/\s/, '-').gsub(/[áàäâ]/, 'a').gsub(/[éèëê]/, 'e')
  #         .gsub(/[íìïî]/, 'i')
  #         .gsub(/[óòöô]/, 'o')
  #         .gsub(/[úùüû]/, 'u')
  #         .gsub('ñ', 'n')
  #         .gsub('ç', 's')

  #   end
  # end

  # Liquid::Template.register_filter(Jekyll::AssetFilter)

  module Paginate

    class CatsAndTags < Generator

      safe true

      def generate(site)
        site.categories.each do |category|
          build_subpages(site, "category", category)
        end

        site.tags.each do |tag|
          build_subpages(site, "tag", tag)
        end
      end

      def build_subpages(site, type, posts)
        posts[1] = posts[1].sort_by { |p| -p.date.to_f }
        # atomize(site, type, posts)
        paginate(site, type, posts)
      end

      def atomize(site, type, posts)
        path = "/#{type}/" + Utils.slugify(posts[0]).gsub(/\s/, '-').gsub(/[áàäâ]/, 'a').gsub(/[éèëê]/, 'e').gsub(/[íìïî]/, 'i').gsub(/[óòöô]/, 'o').gsub(/[úùüû]/, 'u').gsub('ñ', 'n').gsub('ç', 's')

        #atom = AtomPage.new(site, site.source, path, type, posts[0], posts[1])
        site.pages << atom
      end

      def paginate(site, type, posts)
        pages = Pager.calculate_pages(posts[1], site.config['paginate'].to_i)
        (1..pages).each do |num_page|
          pager = Pager.new(site, num_page, posts[1], pages)
          path = "/#{type}/" + Utils.slugify(posts[0]).gsub(/\s/, '-').gsub(/[áàäâ]/, 'a').gsub(/[éèëê]/, 'e').gsub(/[íìïî]/, 'i').gsub(/[óòöô]/, 'o').gsub(/[úùüû]/, 'u').gsub('ñ', 'n').gsub('ç', 's')

          if num_page > 1
            path = path + "/#{num_page}"
          end
          newpage = GroupSubPage.new(site, site.source, path, type, posts[0])
          newpage.pager = pager
          site.pages << newpage

        end
      end
    end

    class GroupSubPage < Page
      def initialize(site, base, dir, type, val)
        @site = site
        @base = base
        @dir = dir
        @name = 'index.html'

        self.process(@name)
        self.read_yaml(File.join(base, '_layouts'), "group_index.html")
        self.data["grouptype"] = type
        self.data[type] = val
      end
    end

    class AtomPage < Page
      def initialize(site, base, dir, type, val, posts)
        @site = site
        @base = base
        @dir = dir
        @name = 'atom.xml'

        self.process(@name)
        self.read_yaml(File.join(base, '_layouts'), "group_atom.xml")
        self.data[type] = val
        self.data["grouptype"] = type
        self.data["posts"] = posts[0..9]
      end
    end
  end
end

Liquid::Template.register_filter(Jekyll::Slug2Filter)
